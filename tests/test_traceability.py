import csv
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import traceability as t  # noqa: E402

MANUAL = {"MT-001": {"ID": "MT-001", "Requirement": "REQ-A"}}


def req(**kw):
    return {"id": "REQ-A", "automated": [], "manual": [], **kw}


def test_a_fully_covered_requirement_has_no_errors():
    assert t.check([req(automated=["TC_X_001"], manual=["MT-001"])], {"TC_X_001"}, MANUAL) == []


def test_an_unknown_automated_test_is_reported():
    errors = t.check([req(automated=["TC_X_999"])], {"TC_X_001"}, MANUAL)
    assert any("TC_X_999" in e for e in errors)


def test_an_unknown_manual_case_is_reported():
    assert any("MT-404" in e for e in t.check([req(manual=["MT-404"])], set(), MANUAL))


def test_a_manual_case_that_belongs_to_another_requirement_is_reported():
    errors = t.check([req(id="REQ-B", manual=["MT-001"])], set(), MANUAL)
    assert any("belongs to REQ-A" in e for e in errors)


def test_a_requirement_without_any_coverage_is_reported():
    assert any("no coverage" in e for e in t.check([req()], set(), MANUAL))


def test_an_external_note_counts_as_coverage():
    assert t.check([req(external="load tests")], set(), MANUAL) == []


def test_duplicate_requirement_ids_are_reported():
    errors = t.check([req(external="x"), req(external="x")], set(), MANUAL)
    assert any("duplicate" in e for e in errors)


def test_test_ids_are_read_from_all_declaration_styles(tmp_path):
    tests = tmp_path / "client" / "tests"
    tests.mkdir(parents=True)
    (tests / "a.spec.js").write_text(
        "test('TC_A_001: one', () => {});\n"
        "test.fail('TC_A_002: open defect', () => {});\n"
        "appTest(\"TC_A_003: custom wrapper\", () => {});\n"
        "// TC_A_004 only mentioned in a comment\n"
    )
    assert t.automated_ids(tmp_path) == {"TC_A_001", "TC_A_002", "TC_A_003"}


def test_main_exits_1_and_still_writes_the_matrix_when_checks_fail(tmp_path):
    app = tmp_path / "app" / "client" / "tests"
    app.mkdir(parents=True)
    (app / "a.spec.js").write_text("test('TC_A_001: one', () => {});")
    reqs = tmp_path / "r.yml"
    reqs.write_text(yaml.safe_dump({"requirements": [{"id": "REQ-A", "automated": ["TC_A_001", "TC_A_002"], "manual": []}]}))
    manual = tmp_path / "m.csv"
    manual.write_text("ID,Title,Requirement\n")
    out = tmp_path / "out.md"
    code = t.main(["--app-repo", str(tmp_path / "app"), "--requirements", str(reqs), "--manual", str(manual), "--out", str(out)])
    assert code == 1 and out.exists()


def test_the_real_manual_cases_are_well_formed():
    path = Path(__file__).resolve().parent.parent / "test-cases" / "manual-test-cases.csv"
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8")))
    assert rows and len({r["ID"] for r in rows}) == len(rows)
    for r in rows:
        assert all(r[c].strip() for c in ("Title", "Requirement", "Steps", "Expected result", "Status")), r["ID"]
