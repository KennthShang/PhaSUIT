<img src='logo1.png'>

This is the source code of our website [Phage SUITE](https://phage.ee.cityu.edu.hk/result?jobId=PhaSUITE20221120-163201-152075)

Phage SUITE is a python library for phage-related tasks, including phage identification, taxonomy classification, host prediction and lifestyle prediction. We integrate our previous published tools: PhaMer, PhaGCN, CHERRY, and PhaTYP into one program. In addition, we optimized the functions in these program to save computation resourse and time and provided an one-shot mode to run all the pipelines using one command.  Hope you will enjoy it.

If you have any suggestion or problem, feel free to contact me via email: jyshang2-c@my.cityu.edu.hk. Also you can open an issue under this GitHub folder.




# Overview


## Required Dependencies
Detailed package information can be found in `webserver.yaml`

If you want to use the gpu to accelerate the program please install the packages below:
* cuda
* Pytorch-gpu

Search [pytorch](https://pytorch.org/) to find the correct cuda version based on your computer


## Quick install
*Note*: we suggest you to install all the package using conda (both [miniconda](https://docs.conda.io/en/latest/miniconda.html) and [Anaconda](https://anaconda.org/) are ok).

After cloning this respository, you can use anaconda to install the **websever.yaml**. This will install all packages you need with cpu mode. The command is: `conda env create -f websever.yaml -n phasuit`


### Prepare the database and environment
Due to the limited size of the GitHub, we zip the database. Before using phasuit, you need to unpack them using the following commands.

1. When you use PhaMer at the first time
```
cd PhaSUIT/
conda env create -f webserver.yaml -n phasuite
conda activate phasuite


# database
fileid="1hjACPsIOqqcS5emGaduYvYrCzrIpt2_9"
filename="phagesuite_database.zip"
html=`curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}"`
curl -Lb ./cookie "https://drive.google.com/uc?export=download&`echo ${html}|grep -Po '(confirm=[a-zA-Z0-9\-_]+)'`&id=${fileid}" -o ${filename}

# inital files
fileid="1E94ii3Q0O8ZBm7UsyDT_n06YekNtfV20"
filename="phagesuite_parameters.zip"
html=`curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}"`
curl -Lb ./cookie "https://drive.google.com/uc?export=download&`echo ${html}|grep -Po '(confirm=[a-zA-Z0-9\-_]+)'`&id=${fileid}" -o ${filename}

unzip phagesuite_database.zip  > /dev/null
unzip phagesuite_parameters.zip  > /dev/null

# move the script to where the conda located
cp blastxml_to_tabular.py {path_to_conda}/envs/phasuit/bin/blastxml_to_tabular.py
chmod 777 {path_to_conda}/envs/phasuit/bin/blastxml_to_tabular.py

# example
cp blastxml_to_tabular.py ~/miniconda3/envs/phasuit/bin/blastxml_to_tabular.py
chmod 777 ~/miniconda3/envs/phasuit/bin/blastxml_to_tabular.py
```


2. Then, you only need to activate your 'phasuite' environment before using phasuite in the next time.
```
conda activate phasuite
```

## Usage 

### Run all pipelines in one command:

```
python main.py [--contigs INPUT_FA] [--threads NUM_THREAD][--len MINIMUM_LEN] [--rootpth ROOT_PTH] [--out OUTPUT_PTH]  [--midfolder MID_PTH] [--parampth PARAM_PTH] [--dbdir DR]
```

**Options**


      --contigs INPUT_FA
                            input fasta file
      --threads NUM_THREAD
                            Number of threads to run PhaMer (default 8)
      --len MINIMUM_LEN
                            predict only for sequence >= len bp (default 3000)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
      --rootpth ROOT_PTH
                            The folder you want to store the outputs of PhaSUITE (default user_0/)
      --out OUTPUT_PTH
                            The output folder under rootpth. All the prediction will be stored in this folder. (default out/)
      --midfolder MID_PTH
                            The midfolder under rootpth. All the intermediate files will be stored in this folder. (default midfolder/)
      --parampth PARAM_PTH 
                            The pth you store your parameters (default parameters/)
      --dbdir DR
                            An optional path to store the database directory (default database/)


**Example**

Prediction on the example file:

    python main.py --contigs test_contigs.fa --threads 8 --len 3000 --rootpth simple_test --out out/ --dbdir database/ --parampth parameters/

Then, Phage SUITE will run all the sub-functions to generate predictions under the `simple_test/out/` foder:  `phamer_prediction.csv` (phage identification), `phagcn_prediction.csv` (taxonomy classification), `cherry_prediction.csv` (host prediction), and `phatyp_prediction.csv` (lifestyle prediction). 



### Run pipeline seperately:

The only difference between running all pipelines and running single pipelines is the name of the file. Below are the examples:

```
# run PhaMer
python PhaMer_single.py --contigs test_contigs.fa --threads 8 --len 3000 --rootpth simple_test --out out/ --dbdir database/ --parampth parameters/

# run PhaTYP
python PhaTYP_single.py --contigs test_contigs.fa --threads 8 --len 3000 --rootpth simple_test --out out/ --dbdir database/ --parampth parameters/

# run PhaGCN
python PhaGCN_single.py --contigs test_contigs.fa --threads 8 --len 3000 --rootpth simple_test --out out/ --dbdir database/ --parampth parameters/

# run CHERRY
python Cherry_single.py --contigs test_contigs.fa --threads 8 --len 3000 --rootpth simple_test --out out/ --dbdir database/ --parampth parameters/
```



## Running Phage SUITE as a binary file

We are sorry that Phage SUITE currently do not support to run as an env in conda. However, you can still add the path of the *.py files to your system path and run them as binary files:

```
export PATH="{path of the *py files}:$PATH"
```

However, if you do not want to revise the system path, you can run Phage SUITE by passing absolute path. For example, if you placed PhaSUITE/ folder under your home path (home/PhaSUITE/) and your database and parameters are store under PhaSUITE/ (home/PhaSUITE/database/ and home/PhaSUITE/parameters/), then you can run the command line as below:

```
python ~/PhaSUITE/main.py --contigs {where your fasta file located} --threads 8 --len 3000 --rootpth {where you want to store the result} --out out/ --dbdir ~/PhaSUITE/database/ --parampth ~/PhaSUITE/parameters/

#example
python home/PhaSUITE/main.py --contigs /computenodes/node35/team3/my_contigs.fasta --threads 8 --len 3000 --rootpth home/my_contigs_result/ --out out/ --dbdir home/PhaSUITE/database/ --parampth home/PhaSUITE/parameters/
```

 

### Contact

If you have any questions, please email us: jyshang2-c@my.cityu.edu.hk





# Citations

The papers of our PhaSUIT can be found below. If you use PhaSUIT for your research, please use the citations listed below. The citation of PhaSUITE is not yet available. 

* PhaMer (phage identification)

```
Jiayu Shang, Xubo Tang, Ruocheng Guo, Yanni Sun, Accurate identification of bacteriophages from metagenomic data using Transformer, Briefings in Bioinformatics, 2022;, bbac258, https://doi.org/10.1093/bib/bbac258
```

* PhaGCN (taxonomy classification)

```
Jiayu Shang, Jingzhe Jiang, Yanni Sun, Bacteriophage classification for assembled contigs using graph convolutional network, Bioinformatics, Volume 37, Issue Supplement_1, July 2021, Pages i25–i33, https://doi.org/10.1093/bioinformatics/btab293
```

* Cherry (host prediction)

```
Jiayu Shang, Yanni Sun, CHERRY: a Computational metHod for accuratE pRediction of virus–pRokarYotic interactions using a graph encoder–decoder model, Briefings in Bioinformatics, 2022;, bbac182, https://doi.org/10.1093/bib/bbac182
```

* PhaTYP (Lifestyle prediction)

```
Shang, J., Tang, X., & Sun, Y. (2022). PhaTYP: Predicting the lifestyle for bacteriophages using BERT. arXiv preprint arXiv:2206.09693.
```

