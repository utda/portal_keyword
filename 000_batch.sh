echo "*** 001"
python 001_download_data_from_portal.py

echo "*** 002"
python 002_merge_json.py

echo "*** 101"
python 101_create_text_from_json.py

echo "*** 102"
python 102_morphological_analysis.py

echo "*** 103"
python 103_create_keywords.py

echo "*** 301"
python 301_create_html.py