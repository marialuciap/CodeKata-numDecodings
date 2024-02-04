from main import numDecodings
import pytest



def test1():
  s = "12"
  expect = 2
  actual = numDecodings(s)
  assert actual == expect


def test2():
  s = "226"
  expect = 3
  actual = numDecodings(s)
  assert actual == expect


def test3():
  s = "2"
  expect = 1
  actual = numDecodings(s)
  assert actual == expect


def test4():
  s = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
  expect = 3981312
  actual = numDecodings(s)
  assert actual == expect


def test5():
  s = "2303030"
  expect = 0
  actual = numDecodings(s)
  assert actual == expect      