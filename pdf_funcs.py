#!/usr/bin/env python3

# extract_doc_info

from pypdf2 import PdfFileReader


def extract_pdf_info(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        num_of_pages = pdf.getNumPages()

    txt = f'''
    Info about {pdf_path}
    Author:         {info.author}
    Creator:        {info.creator}
    Producer:       {info.producer}
    Subject:        {info.subject}
    Title:          {info.title}
    No. of pages:   {num_of_pages}'''

    print(txt)
    return info


if __name__ == '__main__':
    FPATH = '/home/chrisg/Downloads/exhaust.pdf'
    extract_pdf_info(FPATH)
