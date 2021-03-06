# Bioinformatics: CNV Detection

## Abstract

Copy Number Variation or CNVs allows a substantial duplication or deletion of genomes, which typically ranges between 1 kb to 5 Mb (Onsongo 2016). Some applications of CNVs include detecting intellectual disabilities or genetic disorders (Onsongo, 2016). Earlier generation sequencing techniques are being replaced by next-generation sequencing, or NGS because the speed of the tools and algorithms utilized allows a more substantial amount of DNA sequences to read in a shorter amount of time (Sedlazech 2018). As a result, CNV detection and applications are gradually mitigating error rates and decreasing time complexity per reading due to next-generation sequencing. Advancements in NGS data are improving in detection rate accuracy (Onsongo 2016). CNV detection from NGS data is possible by the implementation of a machine learning model, copy number variation-random forest, or CNV-RF (Onsongo 2016). CNV detection is important because this approach of genome manipulation allows one to detect genetic issues in an individual, such as cancer. This study emphasizes CNV detection in comparison to other methods that can detect diseases in individuals because CNVs are becoming more popular in the Bioinformatics field and can potentially detect genetic issues before symptoms of a disease are explicitly illustrated (Zare 2017). These developments serve to answer how diseases can be detected early in individuals from CNVs with a meager error rate. With these developments, CNV detection is generally improving in terms of run-time and accuracy; however, there are occasional pitfalls in these new approaches that will hopefully improve as the field of Bioinformatics advances overtime.

## Methods/Data

<img width="324" alt="Screen Shot 2019-12-29 at 2 32 07 PM" src="https://user-images.githubusercontent.com/27433542/71561729-3301f680-2a48-11ea-80ab-05f35039efe6.png">

Figure 1. This workflow illustrates the CNV-RF algorithm process to find Candidate CNVs (Onsongo, 2016).

This workflow begins by preprocessing. In preprocessing the data, BWA and BowTie 2 serve as reading aligners, which maps sequence readings (Onsongo 2016). BAM files are converted to pileups, which were then utilized by SAMtools to find any potential CNV candidates (Onsongo 2016). SAM is a Sequence Alignment Map that is used to store the sequence readings from BWA and BowTie 2. BAM is similar but follows a Binary reading format. SAMtools allows one to analyze and utilize information from reads in the SAM format. By using BWA and BowTie 2, the ratio is approximately 1.0, which essentially indicates that there are nearly no mappability problems (Onsongo 2016). Accurate mappability is essential because this mitigates error rates when detecting CNVs. After that, the data continues preprocessing by data smoothing with sliding windows (Onsongo 2016). Data smoothing allows the removal of anomalies in datasets to illustrate more evident trends. Coverage ratios were then scaled and smoothed to average values between 0.9 and 1.1 by a sliding 200-bp window (Onsongo 2016). These preprocessing techniques and tools used to generate these values can improve the accuracy of CNV detection when identifying candidates from CNV-RF.
After preprocessing, the exons undergo segmentation and detection to identify which segments will proceed to the filtration process (Onsongo 2016). Next, filtration ensures mitigation in mappability issues by discarding track values that have a coverage ratio under 0.9 and above 1.1 (Onsongo 2016). Furthermore, heterozygous and homozygous deletions and duplications undergo filtering. Heterozygous data, which contains two different alleles, are filtered out if the window average coverage is <20x, while homozygous data, which includes two of the same allele, are filtered out if the window average coverage is <20x (Onsongo 2016). This step of the workflow is essential when implementing a CNV-RF algorithm for accurate CNV detection.

## Random Forest Machine Learning Model

<img width="891" alt="Screen Shot 2019-12-29 at 2 32 25 PM" src="https://user-images.githubusercontent.com/27433542/71561747-7eb4a000-2a48-11ea-80a6-03cccba60ed6.png">

Figure 2. An example of a decision tree classifier involving heterozygous deletion validation (Cutler 2012).

Random Forest classification is performed by detecting whether the heterozygous deletions from the filtration step are false positives or true positives (Onsongo 2016). Only heterozygous deletions undergo the CNV-RF model because NGS data can easily detect homozygous and hemizygous deletions from the coverage ratio requirements (Onsongo 2016). Random Forest is a machine learning model that allows the implementation of multiple decision trees, which enables the classification of data in specific datasets.For example, one method of determining whether a heterozygous deletion is a true or false positive is by deciding if the deletion contains a high amount of polymorphism in genomic regions (Fajardo 2012). If the statement is true, then the deletion is a false positive. If the statement is false, then the statement is a true positive. Note that there are multiple classifications
Vashisht 4
 
to determine if a heterozygous deletion is an acceptable candidate. Figure 2 primarily serves as an example of how Random Forest operates. A majority of random forest implementations contain a multitude of these decision trees. Furthermore, this implementation is efficient to use in large databases and promotes a high accuracy in comparison to other algorithms (Cutler 2012). Thus, this approach is a good candidate for CNV detection that can determine signs of cancer in individuals. Whereas heterozygous deletions are used for this machine learning process, homozygous and hemizygous deletions are not because the provided NGS data allows a more natural method of detection (Onsongo 2016). Heterozygous deletions contain recessive disease traits, which assists CNVs in detecting the disease trait (Gambin 2016). The training data used for CNV-RF is qPCR, or real-time polymerase chain reaction (Onsongo 2016). The purpose of qPCR is to create a specified amount of DNA segments while tracking the status of a process in real-time. Using qPCR as training data improves the CNV-RF’s performance when classifying false and true positives from heterozygous deletions.

## DAVID (Database for Annotation, Visualization, and Integrated Discovery)

Another bioinformatics tool that can be utilized for CNV detection is DAVID (Database for Annotation, Visualization, and Integrated Discovery) (Lu 2014). DAVID contains bioinformatics tools that can be utilized to detect liver cancer from CNV-driven genes (Lu 2014). Using a CNV-RF approach and DAVID can be applied to biological questions on how to detect liver cancer in individuals from CNVs. DAVID can serve as a tool to annotate the CNV sites from the classification component ​(Fig. 1)​. Additionally, DAVID can develop filters that the CNV-RF can apply in order to classify false positive and true positive CNVs.

## Issues with Implementation

A potential issue with the ​(Fig. 1) workflow is the high amount of resources to find CNV candidates. This process requires multiple software tools to convert and manipulate the data. As a result, the overall workflow requires many steps. An individual who uses this workflow must be cautious when following this procedure because they may mishandle some required information that can tamper with results. Furthermore, the overall time complexity to implement this workflow is never explicitly mentioned in Onsongo’s research paper. However, the time-complexity to implement RF is somewhat fast. One study implemented RF for a data set containing 50,000 cases, resulting in the RF creating 100 trees in approximately 11 minutes (Cutler 2012).

## Areas for Future Research

Ultimately, the workflow illustrates a suitable method for this research question because the workflow from ​(Fig. 1) demonstrates an approach in which CNV’s can be detected and how a CNV-RF can determine a false positive and a true positive from heterozygous deletions. Thus, this method produces relatively accurate CNV candidates that can be utilized for detecting diseases in an individual’s genetics. A potential idea that can be applied is to implement ddPCR instead of qPCR as the training data. Digital droplet polymerase chain reaction or ddPCR is similar to qPCR but is more precise, sensitive, and accurate when measuring data (McCord). As a result, ddPCR will likely have a lower error rate than qPCR methods when implementing the RF algorithm to develop candidate CNVs ​(Fig. 1).​ As bioinformatics evolves in CNV detection, there may exist the possibility that CNV detection can help advance personalized medicine. Personalized medicine focuses on customized treatment for a person by their specific genetics. Since candidates implementing CNVs can detect diseases from genetic code, there exists a possibility that candidate CNVs can provide opportunities for individuals to receive personalized medicine. This allows early detection and can provide an opportunity to develop preventive measures for the specified disease (Meyers 2011). Future research is required to explore the possibility of CNV detection for personalized medicine. Approaches such as ​(Fig. 1) may serve as a stepping stone in bioinformatics to utilize CNV detection in personalized medicine.

## Works Cited

1) Cutler, Adele, et al. “Random Forests.” ​Ensemble Machine Learning,​ 2012, pp. 157–175.

2) Fajardo, Karin V. Fuentes, et al. “Detecting False-Positive Signals in Exome Sequencing.” Human Mutation​, vol. 33, no. 4, 2012, pp. 609–613.

3) Gambin, Tomasz, et al. “Homozygous and Hemizygous CNV Detection from Exome Sequencing Data in a Mendelian Disease Cohort.” ​Nucleic Acids Research​, 2016.

4) Lu, Xiaojie, et al. “Identification of Copy Number Variation-Driven Genes for Liver Cancer via Bioinformatics Analysis.” ​Oncology Reports​, vol. 32, no. 5, 2014, pp. 1845–1852.

5) Meyer, Urs A. “Welcome to the Journal of Personalized Medicine: A New Open-Access Platform for Research on Optimal Individual Healthcare.” ​Journal of personalized medicine​ vol. 1,1 1-4. 28 Mar. 2011.

6) Onsongo, Getiria, et al. “CNV-RF Is a Random Forest–Based Copy Number Variation Detection Method Using Next-Generation Sequencing.” ​The Journal of Molecular Diagnostics​, vol. 18, no. 6, 2016, pp. 872–881.

7) Sedlazeck, Fritz J. “Piercing the Dark Matter: Bioinformatics of Long-Range Sequencing and Mapping.” ​F1000 - Post-Publication Peer Review of the Biomedical Literature,​ 2018.

8) Zare, Fatima, et al. “An Evaluation of Copy Number Variation Detection Tools for Cancer Using Whole Exome Sequencing Data.” ​BMC Bioinformatics,​ vol. 18, no. 1, 2017.
