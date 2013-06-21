//
//  MA01MemoList.h
//  MemoApp01
//
//  Created by Takahiro Kashiwagi on 13/06/21.
//  Copyright (c) 2013年 Takahiro Kashiwagi. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface MA01MemoList : NSObject

@property (nonatomic, strong) NSMutableArray *memos;

+ (id)savedMemoList;

@end
