from loader import load_invoice
import json
import pytest


data = {
        "invoice_number":"555",
        "vendor":{
            "name":"karol",
            "tax_id":"1111"
        }
    }

CONTENT =json.dumps(data)


def test_load_invoice(tmp_path):
    
    p = tmp_path / "toy_invoice.json"
    p.write_text(CONTENT, encoding="utf-8")
    
    result = load_invoice(p)
    expected = data
    
    assert expected == result


def test_load_invoice_with_no_existing_file(tmp_path):

    p = tmp_path / "toy_invoice.json"

    with pytest.raises(FileNotFoundError):
        load_invoice(p)


def test_load_invoice_with_bad_json(tmp_path):

    p = tmp_path / "toy_invoice.json"
    p.write_text("bad json", encoding="utf-8")

    with pytest.raises(json.decoder.JSONDecodeError):
        load_invoice(p)
