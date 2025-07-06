# bookkeeper 
bookkeeper is a simple and lightweight command-line tool for recording and managing your daily expenses.  
It supports adding, listing, updating, deleting, and visualizing spending records.

## usage
`python main.py -h`
usage: main.py [-h] [--item ITEM] [--amount AMOUNT] [--date DATE] [--category CATEGORY]
               [--uitem UITEM] [--udate UDATE]
               action

positional arguments:
  action               what you do(add/remove/update/show/table/clean)

options:
  -h, --help           show this help message and exit
  --item ITEM          thing detail
  --amount AMOUNT      amount
  --date DATE          work date
  --category CATEGORY  category
  --uitem UITEM        use with update
  --udate UDATE        use with update 

## example
1. add

`python main.py add --item 聚餐 --date 2025-06-26 --amount 300 --category 饮食`
`python main.py add --item 房租 --date 2025-06-30 --amount 2000 --category 租房`
`python main.py table`
┏━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━┳━━━━━━━━━━┓
┃ date       ┃ item ┃ amount ┃ category ┃
┡━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━╇━━━━━━━━━━┩
│ 2025-06-26 │ 聚餐 │ 300    │ 饮食      │
└────────────┴──────┴────────┴──────────┘

2. remove

`python main.py remove --item(required) 聚餐 --date(required) 2025-06-30`
┏━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━┳━━━━━━━━━━┓
┃ date       ┃ item ┃ amount ┃ category ┃
┡━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━╇━━━━━━━━━━┩
│ 2025-06-30 │ 房租 │ 2000   │ 租房     │
└────────────┴──────┴────────┴──────────┘

3. update

`python main.py update --uitem(required) 房租 --udate(required) 2025-06-30 --item 地铁  \ --date 2025-06-20 --amount 10 --category 交通`
┏━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━┳━━━━━━━━━━┓
┃ date       ┃ item ┃ amount ┃ category ┃
┡━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━╇━━━━━━━━━━┩
│ 2025-06-20 │ 地铁 │ 10     │ 交通     │
└────────────┴──────┴────────┴──────────┘


5. show

`python main.py show`
06-20: ¥10     ████████████████████████████████████████████████████████████

6. table

`python main.py table`
┏━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━┳━━━━━━━━━━┓
┃ date       ┃ item ┃ amount ┃ category ┃
┡━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━╇━━━━━━━━━━┩
│ 2025-06-20 │ 地铁 │ 10     │ 交通     │
└────────────┴──────┴────────┴──────────┘
