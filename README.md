# bookkeeper is a cli tool, which can add list and so on to record your cost

## usage
`python main.py -h`
usage: main.py [-h] [--item ITEM] [--amount AMOUNT] [--date DATE]
               [j kategory CATEGORY] [--uitem UITEM] [--udate UDATE]
               action
- action (required)
- --item     (options)
- --date     (required)
- --amount   (options) 
- --category (options) 

## example
1. add
`python main.py add --item lanch --date 2025-06-26 --amount 300 --category eat`
2. remove
`python main.py remove --item(required) xxx --date xxxx-xx-xx(required)`
3. update
`python main.py update --uitem(required) --udate(required) --item xxx  \ --date xxxx-xx-xx --amount xxx --category xxx`
4. list
`python main.py list`
5. show
`python main.py show`