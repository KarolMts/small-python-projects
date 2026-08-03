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

    pdf.cell(0, 8, text=f"Data wystawienia: {data['issue_date']}", align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.cell(0, 8, text=f"Termin płatności: {data['due_date']}", align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)

    pdf.set_font("DejaVu", size=12)
    y = pdf.get_y()
    x_left = pdf.get_x()
    vendor = data["vendor"]
    pdf.multi_cell(85, 10, text=f"Sprzedawca: {vendor['name']}\n Adres: {vendor['address']}\n NIP:{vendor['tax_id']}", align="L",border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.set_xy(x_left + 85 +20, y)
    customer = data["customer"]
    pdf.multi_cell(0, 10, text=f"Nabywca: {customer['name']}\n Adres: {customer['address']}", align="L", border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(40)

    pdf.set_font("DejaVu", size=8)
    pdf.cell(w=38, h=5, text="Nazwa", align="C", border=1)
    pdf.cell(w=25, h=5, text="Ilość", align="C", border=1)
    pdf.cell(w=25, h=5, text="Cena netto", align="C", border=1)
    pdf.cell(w=25, h=5, text="Stawka VAT", align="C", border=1)
    pdf.cell(w=25, h=5, text="Wartość netto", align="C", border=1)
    pdf.cell(w=25, h=5, text="Wartość VAT", align="C", border=1)
    pdf.cell(w=25, h=5, text="Wartość brutto", align="C", border=1, new_x="LMARGIN", new_y="NEXT")

    for item, charge in zip(data['line_items'], charges):
        pdf.cell(w=38, h=5, text=f"{item['description']}", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{item['quantity']}", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{float(item['unit_price']):>,.2f}", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{float(item['tax_rate'])*100}%", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{float(charge.net):>,.2f}", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{float(charge.vat):>,.2f}", align="C", border=1)
        pdf.cell(w=25, h=5, text=f"{float(charge.gross):>,.2f}", align="C", border=1, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(5)
    pdf.set_font("DejaVu", size=12)
    pdf.cell(w=110, h=5, text="Razem:", align="R")
    pdf.cell(w=25, h=5, text=f"{total.net}", align="C", border=1)
    pdf.cell(w=25, h=5, text=f"{total.vat}", align="C", border=1)
    pdf.cell(w=25, h=5, text=f"{total.gross}", align="C", border=1)
    pdf.cell(w=15, h=5, text=f"{data['currency']}", align="C", border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)

    pay = data["payment"]
    pdf.set_font("DejaVu", size=14)
    pdf.cell(w=25, h=5, text=f"Płaność:", align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    pdf.set_font("DejaVu", size=10)

    pdf.set_x(pdf.get_x() + 5)
    pdf.multi_cell(w=0, h=6, text=f"Bank:  {pay['bank']}\nNumer konta:  {pay['account_number']}\nSposób:  {pay['form']}\nTytułem:  {pay['title']}", align="L")

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