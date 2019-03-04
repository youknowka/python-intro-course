#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://makina-corpus.com/blog/metier/2015/python-http-server-with-the-new-async-await-syntax

import asyncio

@asyncio.coroutine
def c1():
    for n in range(3):
        yield from asyncio.sleep(0.5)
        print("c1-%d" % (n))
    print("c2-3")


@asyncio.coroutine
def c2():
    for n in range(3):
        yield from asyncio.sleep(0.5)
        print("c2-%d" % (n))
    print("c2-3")

# OOPS! https://stackoverflow.com/a/49377261/539470
# @asyncio.coroutine
# def test2coroutines1():
#     yield from asyncio.wait([])

@asyncio.coroutine
def test2coroutines2():
    yield from asyncio.wait([
        c1(),
        c2()
    ])


if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test2coroutines2())