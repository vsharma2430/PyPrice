with open('commands\pip.txt', 'r') as f:
    print(' && '.join([line.strip() for line in f.readlines()]))
    
'''
pip install "yfinance[nospam,repair]" && pip install "fastapi[standard]" && pip install uvicorn
'''