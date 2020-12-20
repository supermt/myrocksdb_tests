import csv
import json
import pandas as pd
import os

import zipfile


# Macros
DATA_DIR_PREFIX = "/media/jinghuan/nvme/OpenAcademicData"
FILENAME = "/mag_venues.txt"
SEGMENT_SIZE = 1 * 1000 * 1000
REPORT_GAP = 10000

table_column_order = {
    "mag_venues": ["id", "DisplayName", "NormalizedName", "JournalId", "ConferenceId"],
    "mag_papers_0": ["id","title","n_citation","doc_type"]

}