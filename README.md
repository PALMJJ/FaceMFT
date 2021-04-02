# multiple face tracking 多人脸跟踪模型FaceMFT

* 博客：https://blog.csdn.net/qq_25808521/article/details/114970053?spm=1001.2014.3001.5501
* MobileNet模型地址：链接：https://pan.baidu.com/s/1xNS5m_0tNMhUSftu5M69kA 提取码：r2w5
* 训练模型地址：链接：https://pan.baidu.com/s/1t93KllfScpWVL5OMUCFt-g 提取码：2z6w
* 数据集地址：链接：https://pan.baidu.com/s/1KMt7u-Su84VQ2N7pw2Sw1g 提取码：ex4i

## Installation

* Clone this repo, and we'll call the directory that you cloned as ${FAIRMOT_ROOT}
* Install dependencies. We use python 3.7 and pytorch >= 1.2.0

```
conda create -n FairMOT
conda activate FairMOT
conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=10.0 -c pytorch
cd ${FAIRMOT_ROOT}
pip install -r requirements.txt
```

* We use [DCNv2](https://github.com/CharlesShang/DCNv2) in our backbone network and more details can be found in their repo. 

```
git clone https://github.com/CharlesShang/DCNv2
cd DCNv2
./make.sh
```

* In order to run the code for demos, you also need to install [ffmpeg](https://www.ffmpeg.org/).

## Data preparation

* **CrowdHuman**
  The CrowdHuman dataset can be downloaded from their [official webpage](https://www.crowdhuman.org). After downloading, you should prepare the data in the following structure:

```
crowdhuman
   |——————images
   |        └——————train
   |        └——————val
   └——————labels_with_ids
   |         └——————train(empty)
   |         └——————val(empty)
   └------annotation_train.odgt
   └------annotation_val.odgt
```

Then, you can change the paths in src/gen_labels_crowd.py and run:

```
cd src
python gen_labels_crowd.py
```

* **MIX**
  We use the same training data as [JDE](https://github.com/Zhongdao/Towards-Realtime-MOT) in this part and we call it "MIX". Please refer to their [DATA ZOO](https://github.com/Zhongdao/Towards-Realtime-MOT/blob/master/DATASET_ZOO.md) to download and prepare all the training data including Caltech Pedestrian, CityPersons, CUHK-SYSU, PRW, ETHZ, MOT17 and MOT16. 
* **2DMOT15 and MOT20** 
  [2DMOT15](https://motchallenge.net/data/2D_MOT_2015/) and [MOT20](https://motchallenge.net/data/MOT20/) can be downloaded from the official webpage of MOT challenge. After downloading, you should prepare the data in the following structure:

```
MOT15
   |——————images
   |        └——————train
   |        └——————test
   └——————labels_with_ids
            └——————train(empty)
MOT20
   |——————images
   |        └——————train
   |        └——————test
   └——————labels_with_ids
            └——————train(empty)
```

Then, you can change the seq_root and label_root in src/gen_labels_15.py and src/gen_labels_20.py and run:

```
cd src
python gen_labels_15.py
python gen_labels_20.py
```

to generate the labels of 2DMOT15 and MOT20. The seqinfo.ini files of 2DMOT15 can be downloaded here [[Google]](https://drive.google.com/open?id=1kJYySZy7wyETH4fKMzgJrYUrTfxKlN1w), [[Baidu],code:8o0w](https://pan.baidu.com/s/1zb5tBW7-YTzWOXpd9IzS0g).

## Pretrained models and baseline model

* **Pretrained models**

DLA-34 COCO pretrained model: [DLA-34 official](https://drive.google.com/file/d/1pl_-ael8wERdUREEnaIfqOV_VF2bEVRT/view).
HRNetV2 ImageNet pretrained model: [HRNetV2-W18 official](https://1drv.ms/u/s!Aus8VCZ_C_33cMkPimlmClRvmpw), [HRNetV2-W32 official](https://1drv.ms/u/s!Aus8VCZ_C_33dYBMemi9xOUFR0w).
After downloading, you should put the pretrained models in the following structure:

```
${FAIRMOT_ROOT}
   └——————models
           └——————ctdet_coco_dla_2x.pth
           └——————hrnetv2_w32_imagenet_pretrained.pth
           └——————hrnetv2_w18_imagenet_pretrained.pth
```

* **Baseline model**

Our baseline FairMOT model (DLA-34 backbone) is pretrained on the CrowdHuman for 60 epochs with the self-supervised learning approach and then trained on the MIX dataset for 30 epochs. The models can be downloaded here: 
crowdhuman_dla34.pth [[Google]](https://drive.google.com/file/d/1SFOhg_vos_xSYHLMTDGFVZBYjo8cr2fG/view?usp=sharing) [[Baidu, code:ggzx ]](https://pan.baidu.com/s/1JZMCVDyQnQCa5veO73YaMw) [[Onedrive]](https://microsoftapc-my.sharepoint.com/:u:/g/personal/v-yifzha_microsoft_com/EUsj0hkTNuhKkj9bo9kE7ZsBpmHvqDz6DylPQPhm94Y08w?e=3OF4XN).
fairmot_dla34.pth [[Google]](https://drive.google.com/file/d/1iqRQjsG9BawIl8SlFomMg5iwkb6nqSpi/view?usp=sharing) [[Baidu, code:uouv]](https://pan.baidu.com/s/1H1Zp8wrTKDk20_DSPAeEkg) [[Onedrive]](https://microsoftapc-my.sharepoint.com/:u:/g/personal/v-yifzha_microsoft_com/EWHN_RQA08BDoEce_qFW-ogBNUsb0jnxG3pNS3DJ7I8NmQ?e=p0Pul1). (This is the model we get 73.7 MOTA on the MOT17 test set. )
After downloading, you should put the baseline model in the following structure:

```
${FAIRMOT_ROOT}
   └——————models
           └——————fairmot_dla34.pth
           └——————...
```

## Training

* Download the training data
* Change the dataset root directory 'root' in src/lib/cfg/data.json and 'data_dir' in src/lib/opts.py
* Pretrain on CrowdHuman and train on MIX:

```
sh experiments/crowdhuman_dla34.sh
sh experiments/mix_ft_ch_dla34.sh
```

* Only train on MIX:

```
sh experiments/mix_dla34.sh
```

* Only train on MOT17:

```
sh experiments/mot17_dla34.sh
```

* Finetune on 2DMOT15 using the baseline model:

```
sh experiments/mot15_ft_mix_dla34.sh
```

* Finetune on MOT20 using the baseline model:

```
sh experiments/mot20_ft_mix_dla34.sh
```

* For ablation study, we use MIX and half of MOT17 as training data, you can use different backbones such as ResNet, ResNet-FPN, HRNet and DLA:

```
sh experiments/mix_mot17_half_dla34.sh
sh experiments/mix_mot17_half_hrnet18.sh
sh experiments/mix_mot17_half_res34.sh
sh experiments/mix_mot17_half_res34fpn.sh
sh experiments/mix_mot17_half_res50.sh
```

* Performance on the test set of MOT17 when using different training data:

| Training Data    | MOTA | IDF1 | IDS  |
| ---------------- | ---- | ---- | ---- |
| MOT17            | 69.8 | 69.9 | 3996 |
| MIX              | 72.9 | 73.2 | 3345 |
| CrowdHuman + MIX | 73.7 | 72.3 | 3303 |

## Tracking

* The default settings run tracking on the validation dataset from 2DMOT15. Using the baseline model, you can run:

```
cd src
python track.py mot --load_model ../models/fairmot_dla34.pth --conf_thres 0.6
```

to see the tracking results (76.5 MOTA and 79.3 IDF1 using the baseline model). You can also set save_images=True in src/track.py to save the visualization results of each frame. 

* For ablation study, we evaluate on the other half of the training set of MOT17, you can run:

```
cd src
python track.py mot --load_model ../exp/mot/mix_mot17_half_dla34.pth --conf_thres 0.4
```

* To get the txt results of the test set of MOT16 or MOT17, you can run:

```
cd src
python track.py mot --test_mot17 True --load_model ../models/fairmot_dla34.pth --conf_thres 0.4
python track.py mot --test_mot16 True --load_model ../models/fairmot_dla34.pth --conf_thres 0.4
```

and send the txt files to the [MOT challenge](https://motchallenge.net) evaluation server to get the results. (You can get the SOTA results 73+ MOTA on MOT17 test set using the baseline model 'fairmot_dla34.pth'.)

* To get the SOTA results of 2DMOT15 and MOT20, run the tracking code:

```
cd src
python track.py mot --test_mot15 True --load_model your_mot15_model.pth --conf_thres 0.3
python track.py mot --test_mot20 True --load_model your_mot20_model.pth --conf_thres 0.3
```

Results of the test set all need to be evaluated on the MOT challenge server. You can see the tracking results on the training set by setting --val_motxx True and run the tracking code. We set 'conf_thres' 0.4 for MOT16 and MOT17. We set 'conf_thres' 0.3 for 2DMOT15 and MOT20. 

## Demo

You can input a raw video and get the demo video by running src/demo.py and get the mp4 format of the demo video:

```
cd src
python demo.py mot --load_model ../models/fairmot_dla34.pth --conf_thres 0.4
```

You can change --input-video and --output-root to get the demos of your own videos.
--conf_thres can be set from 0.3 to 0.7 depending on your own videos.
