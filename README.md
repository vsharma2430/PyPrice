### Introduction 

PyPrice is a web API to fetch current market prices by scraping Yahoo Finance.

#### Features
- Live stock/ETF prices 

#### Dependencies
- Fastapi
- Yfinance

### Installation Instructions

- Download and Install Python 3.12+ from [Official Python website](https://www.python.org/downloads/)
- Create a folder in your system 'PyPrice'.
- Open terminal/command prompt in the folder location.
- Clone this Git Repository to a desired folder.

```custom_prefix(E:\PyPrice>)
git clone https://github.com/vsharma2430/PyPrice
```
- Create virtual environment for this project.

```custom_prefix(E:\PyPrice>)
python -m venv .venv
```
- Activate virtual environment.
```custom_prefix(E:\PyPrice>)
E:\PyPrice\.venv\Scripts\Activate.ps1
```
- Install dependencies.
```custom_prefix((.venv) E:\PyPrice>)
pip install -r requirements.txt
```
- Run client.py
```custom_prefix((.venv) E:\PyPrice>)
python client.py
```