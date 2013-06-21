//
//  MA01MemoList.m
//  MemoApp01
//
//  Created by Takahiro Kashiwagi on 13/06/21.
//  Copyright (c) 2013年 Takahiro Kashiwagi. All rights reserved.
//

#import "MA01MemoList.h"

@implementation MA01MemoList

+ (id)savedMemoList {
    static dispatch_once_t pred = 0;
    __strong static id _savedObject = nil;
    dispatch_once(&pred, ^{
        _savedObject = [[self alloc] init];
    });
    return _savedObject;
}

- (id)init {
    
    self = [super init];
    if (!self) {
        return nil;
    }
    
    self.memos = [[NSMutableArray alloc] init];
    return self;
}


@end
