#! /usr/bin/python
# -*- coding: utf-8 -*-

print ("モジュールのロード")

def test():
  print "関数：testを呼び出しました"

if __name__ == "__main__":

  print "python-izm"
  test()

test_str = """
test1
test2
"""

print test_str

test_str = 'python'
test_str = test_str + "-"
test_str = test_str + "izm"

print test_str

print test_str.split("-")

print test_str.rjust(20, "0")
print test_str.rjust(20, "!")

print test_str.zfill(40)

print test_str.startswith("python")
print test_str.startswith("izm")

print "z" in test_str
print "s" in test_str

print test_str.upper()
print test_str.lower()
print test_str


test_int = 199
print str(test_int) + "ほげ"