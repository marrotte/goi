## Synopsis

Output games of interest (GOI) for sports betting.

## How it works

Scrapes the **edge** games out of statfox (http://www.statfox.com)

## Motivation

The power rating system is based on recent game results. The relative strength of the two teams involved is compared. A power line is calculated using both teams ratings and home field advantage. Where the power line differs significantly from the current line, the team with the edge is indicated.

## Requirements
Python <br>
PIP (https://pip.pypa.io/en/stable/installing/)

## Install
    git clone https://github.com/marrotte/goi.git
    cd goi
    pip install -r requirments.txt

## Usage
### Help
    $ ./goi.py -h
    GIO (Games of Interest), Version 4.0
    gio.py -s[--sport] <sport>
    supported sports are cbb, nba, cfl, and mlb
### College basketball
    $ ./goi.py -s cbb
    Saturday at  2:30 PM
    MARQUETTE 160
    CREIGHTON -5 (-11 powerspread), edge

    Saturday at  10:00 PM
    UC-IRVINE 147.5 (-10 powerspread), edge
    CS-NORTHRIDGE +3.5

These two games of interest show that Creighton and UC-Irvine have the edge as explained, above by statfox.  Creighton is a 5 point favorite over Marquette and the power rating has them as an 11 point favorite.  Likewise, UC-Irvine is a 3.5 point favorite over CS-Northridge and the power rating has them as a 10 point favorite.  The Creighton games is on this Saturday at 2:30PM and the UC-Irvine at 10PM.  The money line is 160 in the Creighton game and 147.5 in the UC-Irvine game.

## License

Copyright 2016 marrotte

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
