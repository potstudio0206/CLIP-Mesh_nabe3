import subprocess
import time
COCO_list = open('./word/COCO.txt','r').read().split("\n")
text_list = ["an apple","a wooden table"]
epochs = [2500,5000,7500]
learning_rate = [0.001,0.01,0.1]
batch_size = [25,50,75]
i = 0

#for num_text in range(len(text_list)):
#    for num_epoch in range(len(epochs)):
#        for num_lr in range(len(learning_rate)):
#            for num_batch in range(len(batch_size)):
#                epoch = epochs[num_epoch]
#                lr = learning_rate[num_lr]
#                text = text_list[num_text]
#                batch = batch_size[num_batch]
#                output_path = "/outputs/"+ str(text) +"_" + str(epoch) + "_" + str(lr) +"_"+ str(batch) +"/"
#                cmd = 'python /clipmesh/main.py --config configs/single2jp.yml  --text_prompt \"{0}\" --output_path \"{1}\" --epochs {2} --lr {3} --batch_size {4}'.format(text,output_path,epoch,lr,batch)
#                subprocess.run(cmd,shell=True,stderr=subprocess.STDOUT)
#                i += 1
#                print(str(i) + "回目")
print("sleeping an hour...")
time.sleep(60*60)

for num_text in range(len(text_list)):
    for num_epoch in range(len(epochs)):
        for num_lr in range(len(learning_rate)):
            for num_batch in range(len(batch_size)):
                epoch = epochs[num_epoch]
                lr = learning_rate[num_lr]
                text = text_list[num_text]
                batch = batch_size[num_batch]
                output_path = "/outputs_old/"+ str(text) +"_" + str(epoch) + "_" + str(lr) +"_"+ str(batch) +"/"
                cmd = 'python /clipmesh/mains.py --config configs/single2jp.yml  --text_prompt \"{0}\" --output_path \"{1}\" --epochs {2} --lr {3} --batch_size {4}'.format(text,output_path,epoch,lr,batch)
                subprocess.run(cmd,shell=True,stderr=subprocess.STDOUT)
                i += 1
                print(str(i) + "回目")
                print("sleeping 3 mins...")
                time.sleep(60*3)
