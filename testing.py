from htmldate import find_date
test='https://core.ac.uk/download/pdf/147637727.pdf'
def validate_date(test):
    document_y_or_n=test.split('/')[-1]
    pdf_y_or_n=test.split('.')[-1]
    print(pdf_y_or_n or)
    if(pdf_y_or_n=='pdf' or document_y_or_n='document'):
        return ''
    return find_date(item["link"]) if find_date(item["link"]) else ""
print(validate_date(test))