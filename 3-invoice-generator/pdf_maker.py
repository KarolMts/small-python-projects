from fpdf import FPDF
from accountant import calculate, summarize
from pathlib import Path

FONT = Path(__file__).resolve().parent / "fonts" / "DejaVuSans.ttf"

class InvoicePDF(FPDF):
    def __init__(self, data):
        super().__init__()
        self.add_font("DejaVu", fname=str(FONT))
        self.data = data

    def header(self) -> None:
        self.set_font("DejaVu", size=16)
        self.cell(0, 10, text=f"Faktura nr {self.data['invoice_number']}", align="C", border=1, new_x="LMARGIN", new_y="NEXT")
        self.ln(10)

    def footer(self) -> None:
        self.set_y(-15)
        self.set_font("DejaVu", size=8)
        self.cell(0, 10, f"Strona {self.page_no()}/{{nb}}", align='C')



def create_pdf(data, charges, total):
    pdf = InvoicePDF(data)
    pdf.add_page()

    vendor = data["vendor"]
    pdf.multi_cell(0, 10, text=f"Sprzedawca: {vendor['name']} {vendor['address']} {vendor['tax_id']}", align="L",border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    customer = data["customer"]
    pdf.multi_cell(0, 10, text=f"Nabywca: {customer['name']} {customer['address']}", align="L", border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.set_font("DejaVu", size=8)
    pdf.cell(w=35, h=5, text="Nazwa", align="C", border=1)
    pdf.cell(w=25, h=5, text="Ilość", align="C", border=1)
    pdf.cell(w=25, h=5, text="Cena netto", align="C", border=1)
    pdf.cell(w=25, h=5, text="Stawka VAT", align="C", border=1)
    pdf.cell(w=25, h=5, text="Wartość netto", align="C", border=1)
    pdf.cell(w=25, h=5, text="Wartość VAT", align="C", border=1)
    pdf.cell(w=25, h=5, text="Wartość brutto", align="C", border=1, new_x="LMARGIN", new_y="NEXT")

    for item, charge in zip(data['line_items'], charges):
        pdf.cell(w=35, h=5, text=f"{item['description']}", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{item['quantity']}", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{item['unit_price']}", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{item['tax_rate']}", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{charge.net}", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{charge.vat}", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{charge.gross}", align="C", border=1, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(2)
    pdf.set_font("DejaVu", size=12)
    pdf.cell(w=110, h=5, text="Razem:", align="R")
    pdf.cell(w=25, h=5, text=f"{total.net}", align="C", border=1)
    pdf.cell(w=25, h=5, text=f"{total.vat}", align="C", border=1)
    pdf.cell(w=25, h=5, text=f"{total.gross}", align="C", border=1)
    pdf.cell(w=15, h=5, text=f"{data['currency']}", align="C", border=1)

    pdf.output("faktura.pdf")


# hidding test-harness under the guard
if __name__ == "__main__":

    test_data={
        "invoice_number":"P/43917324/0001/26",
        "issue_date":"2026-02-02",
        "due_date":"2026-02-16",
        "currency":"PLN",
        "vendor":{
            "name":"hard_ware_company",
            "address":"ul.Jana Kazimierza 3, 01-248 Warszawa",
            "tax_id":"5272706082"
        },
        "customer":{
            "name":"some client",
            "address":"some address"
        },
        "line_items":[
            {
                "description":"laptop hd omen",
                "quantity":4,
                "unit_price":"5400.00",
                "tax_rate":"0.23"
            },
            {
                "description":"computer mouse logitech",
                "quantity":2,
                "unit_price":"399.00",
                "tax_rate":"0.08"
            }
        ],
        "payment":{
            "bank":"Bank Pekao S.A.",
            "account_number":"02 1240 6960 0162 2190 8829 0006",
            "form":"transfer",
            "title":"shopping"
        }
    }

    charges = [
                        calculate(vat_rate=item['tax_rate'], unit_price=item['unit_price'], quantity=item['quantity'])
                        for item in test_data['line_items']
                      ]

    total = summarize(charges)

    create_pdf(test_data, charges, total)