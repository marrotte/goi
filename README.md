## Synopsis

Outputs game of interest (GOI) for sports betting.

## How it works

Scrapes the **edge** games out of statfox (http://www.statfox.com)

## Motivation

The power rating system is based on recent game results. The section should be used to compare the relative strength of the two teams involved. A power line is calculated using both teams ratings and home field advantage. Where the power line differs significantly from the current line, the team with the edge is indicated.

## Usage
    $ ./goi.py -h
    GIO (Games of Interest), Version 4.0
    gio.py -s[--sport] <sport>
    supported sports are cbb, nba, cfl, and mlb```

## License

Copyright 2016 marrotte

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
