//
//  MA01ViewController.m
//  MemoApp01
//
//  Created by Takahiro Kashiwagi on 13/06/21.
//  Copyright (c) 2013年 Takahiro Kashiwagi. All rights reserved.
//

#import "MA01ViewController.h"
#import "MA01Memo.h"
#import "MA01MemoLIst.h"

@interface MA01ViewController ()
@property (weak, nonatomic) IBOutlet UITextField *memotext;

@end

@implementation MA01ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)createMemo:(id)sender {
    MA01Memo *memo = [[MA01Memo alloc] init];
    memo.title = self.memotext.text;
    
    [[[MA01MemoList savedMemoList] memos] addObject:memo];
}
@end
