import dataloader

def testTrainingImages():

    class TestOpts():
        def __init__(self):
            self.batch_size = 5
            self.datasets_dir = '/home/fsb1/git/pytorch-CycleGAN-and-pix2pix/datasets'
            self.dataset = 'apple2orange'
    
    opts = TestOpts()
    loader = dataloader.forTraining(opts)
 
    for batch in loader:
        print('batchA', batch['A'].shape)
        print('batchB', batch['B'].shape)
        break
    
if __name__ == '__main__':
    testTrainingImages()