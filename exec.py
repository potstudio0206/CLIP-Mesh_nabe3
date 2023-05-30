import subprocess
COCO_list = open('./word/COCO.txt','r').read().split("\n")
epochs = [2500,5000]
learning_rate = [0.001,0.01,0.1]
i = 0

for COCO_type in range(len(COCO_list)):
    for num_epoch in range(len(epochs)):
        for num_lr in range(len(learning_rate)):
            epoch = epochs[num_epoch]
            lr = learning_rate[num_lr]
            text = COCO_list[COCO_type]
            output_path = "/outputs/"+COCO_list[COCO_type] +"_" + str(epoch) + "_" + str(lr) + "/"
            cmd = 'python /clipmesh/main.py --config configs/single2jp.yml  --text_prompt \"{0}\" --output_path \"{1}\" --epochs {2} --lr {3}'.format(text,output_path,epoch,lr)
            subprocess.run(cmd,shell=True,stderr=subprocess.STDOUT)
            i += 1
            print(str(i) + "回目")