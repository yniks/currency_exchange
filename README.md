# currency_exchange
Quick Utility to convert currency values

# USAGE:
```bash
usage: exhange.py [-h] [-v] from value to
exhange.py: error: the following arguments are required: from, value, to
```
## example
```bash
python3 exchange.py inr 23 pkr
`10.686036556345238`
```
## --verbose

```bash
python3 exchange.py inr 23 pkr --verbose
`2021-03-10 20:34:27.643890 :: loading file for today
2021-03-10 20:34:27.644278 :: loaded data from filesystem
2021-03-10 20:34:27.644378 :: Converting Indian Rupee to Pakistani Rupee
2021-03-10 20:34:27.644465 :: 23.0 Indian Rupee equals 10.686036556345238 Indian Rupee
10.686036556345238`
```
