# Labadain Crawler


## Overview

Labadain crawler is a data collection pipeline for low-resource languages designed to automate and optimize the process of constructing comprehensive textual corpora from the web. The system is built on top of the Apache Nutch framework and incorporates language-specific components such as a tokenizer and a language identification model.


## Requirements

### Technical requirements
- [ ] Apache Nutch.
- [ ] Apache Solr.

### Language specific requirements
- [ ] An initial text corpus containing the target language.
- [ ] A tokenizer.
- [ ] A language identification model.


## Getting started

- [ ] Create a project folder and name it `crawler-home`.
- [ ] Navigate into the project folder, create a virtual environment and activate it.
- [ ] Clone the pipeline's source codes:

```
$ git clone https://github.com/gabriel-de-jesus/labadain-crawler.git

```

- [ ]  Install the dependencies specified in the `requirements` file.

```
pip install -r requirements.txt
```


## Apache Nutch and Solr Setup

To set up Apache Nutch and Solr, follow these steps:

- [ ] **Download Apache Nutch and Solr:** download the Apache Nutch and Solr packages and save them into the **crawler-home** directory. Ensure that you download the appropriate version compatible with your system.

- [ ] **Configure Apache Nutch:** refer to the [Nutch installation and configuration tutorial](https://cwiki.apache.org/confluence/display/NUTCH/NutchTutorial) for detailed instructions on how to configuring Nutch. Follow the tutorial, but skip the **Crawl your first website** section and proceed directly to the **Setup Solr for search** section.

- [ ] **Rename the Nutch and Solr packages:** after downloading and extracting the packages, rename the Nutch package directory from `apache-nutch-1.x` to `nutch` and the Solr package directory from `apache-solr-9.x` to `solr`.

- [ ] **Verify the Nutch and Solr configurations:** after completing the configuration steps, verify that both Nutch and Solr are working correctly. You can do this by following the verification steps provided in the tutorial.


## Pipeline Setup

To set up the pipeline, you need to organize the following main folders in the specified structure:

- [ ] **pipeline**: this folder contents include codes for configuration, seeder, corpus construction, and corpus summary generation. It also contains the lid, data, and log folders.
- [ ] **nutch**: it contains the Nucth framework files.
- [ ] **solr**: it contains the Solr framework files.


### Create folders and copy the LID model and initial corpus

- [ ] Create the LID, data, and log folders within the pipeline folder. 
- [ ] Copy the LID model, name it `lid_model.pkl`, and locate it in the **lid** folder. 
- [ ] Copy the initial corpus, name it `initial_corpus.txt`, and locate it in the **data** folder.

`[Optional]`

If you want to use the module to generate a data sample for evaluation purposes, you can create an additional folder inside the **data directory** and name it `evaluation_sampl`. This folder will be used to store the generated data sample.


### Module Configuration

In the configuration folder, you will find the general pipeline configuration located in **pipeline/conf/config.yaml**. This configuration module consists of the following components:


- [ ] **files:** This section contains files that are either required by the pipeline or will be generated by the pipeline.
- [ ] **paths:** This section contains paths that are either required by the pipeline or will be generated by the pipeline.
- [ ] **params:** The configurations in this group and the following sections can be adjusted according to your specific requirements. This includes settings related to Solr, language processing, LID model, corpus used by the pipeline, and extensions.


### LID Model Configuration

To configure the language identification (LID) model in the pipeline, follow these steps:

- [ ] Open the file **pipeline/common_utils/tetun_lid.py**.
- [ ] Locate the `get_tetun_text` function within the file.
- [ ] Adjust the function according to the nature of your LID model.
- [ ] **Ensure that the function receives a list of strings as input.** This is important to optimize the corpus construction process and make it faster. Undertake the necessary modifications to the `get_tetun_text` function based on your LID model's requirements.


## Pipeline Execution

To execute the pipeline and initiate the crawling process, follow these steps:

- [ ] On the `crawler-home` directory, run the file named `labadain_crawler.py` using the following command :

```
python3 labadain_crawler.py
```

**Note:** The default values are 5 for `seeder repetitions` and 1 for `crawling repetitions`. You can adjust these parameters, for example, by setting `seeder repetitions to 10` and `crawling repetitions to 5` as follows:

```
python3 labadain_crawler.py --seeder-runs 10 --crawl-runs 5
```

To skip some stages such as `seeder` and `crawling`, you can use `skip` parameter:

```
python3 labadain_crawler.py --skip-seeder --skip-crawl
```

Running this command will execute the pipeline and automatically start the crawling process.


## Citation
If you use this repository or any of its contents for your research, academic work, or publication, please cite it as follows:

````
@inproceedings{de-jesus-nunes-2024-labadain-crawler,
    title = "Data Collection Pipeline for Low-Resource Languages: A Case Study on Constructing a Tetun Text Corpus",
    author = "de Jesus, Gabriel  and
      Nunes, S{\'e}rgio Sobral",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.390",
    pages = "4368--4380"
}
````

## Acknowledgement
This work is financed by National Funds through the Portuguese funding agency, FCT - Fundação para a Ciência e a Tecnologia under the PhD studentship grant number SFRH/BD/151437/2021 (DOI 10.54499/SFRH/BD/151437/2021).


## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/gabriel-de-jesus/labadain-crawler/blob/main/LICENSE)


## Contact Information
If you have any questions or feedback, please feel free to contact mestregabrieldejesus[at]gmail.com.
