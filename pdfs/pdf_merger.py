#!/usr/bin/env python3

# extract_doc_info

import glob
import os
import time
from PyPDF2 import PdfFileReader, PdfFileWriter


def extract_pdf_info(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        num_of_pages = pdf.getNumPages()

    txt = f'''
    Info about {os.path.basename(pdf_path)}
    Author:         {info.author}
    Creator:        {info.creator}
    Producer:       {info.producer}
    Subject:        {info.subject}
    Title:          {info.title}
    No. of pages:   {num_of_pages}'''

    print(txt)
    return info, num_of_pages


def text_extractor(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)

        page = pdf.getPage(2)
        print(page)
        print('Page type: {}'.format(str(type(page))))


def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()

    for path in input_paths[:1]:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output_path, 'wb') as outfile:
        pdf_writer.write(outfile)


if __name__ == '__main__':
    #  paths = glob.glob('*.pdf')
    #  paths.sort()
    with open('../pdf.lst', 'r') as file:
        pdf_lst = file.read().splitlines()

    #  print(pdf_lst)
    merger('pdf_merger.pdf', pdf_lst)
