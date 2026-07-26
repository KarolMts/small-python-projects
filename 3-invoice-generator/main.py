import sys
import argparse
import json
from loader import load_invoice
from accountant import calculate, summarize

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('file', help = 'path to invoice')
    args = parser.parse_args()

    try:
        data = load_invoice(args.file)
        charges = [
                    calculate(vat_rate=item['tax_rate'], unit_price=item['unit_price'], quantity=item['quantity'])
                    for item in data['line_items']
                  ]
        total = summarize(charges)
    except FileNotFoundError:
        sys.exit('File not found')
    except json.decoder.JSONDecodeError:
        sys.exit('Incorrect format')
    except KeyError as e:
        sys.exit(f'Key {e} not found')

    else:
        print(f"{'netto':<8}{total.net:>12,.2f} {data['currency']}")
        print(f"{'vat':<8}{total.vat:>12,.2f} {data['currency']}")
        print(f"{'brutto':<8}{total.gross:>12,.2f} {data['currency']}")
        print(charges)


if __name__ == '__main__':
    main()