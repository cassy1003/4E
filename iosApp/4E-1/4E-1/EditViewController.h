//
//  EditViewController.h
//  4E-1
//
//  Created by toru.furuya on 13/05/31.
//
//

#import <UIKit/UIKit.h>

@interface EditViewController : UIViewController

@property (weak, nonatomic) IBOutlet UILabel *labelText;
@property (weak, nonatomic) IBOutlet UITextView *labelTextBox;
- (IBAction)saveButton:(id)sender;
@end
