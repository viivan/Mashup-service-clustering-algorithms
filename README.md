# Mashup-service-clustering-algorithms
包含T+Q、T+K、LDA、L+K、F+K、F+C+D、F+C+K算法代码，方法的具体介绍如下：

T+Q：该方法将每个Mashup服务描述文本转化为TF-IDF特征向量进行QT聚类。

T+K：该方法也是先利用TF-IDF技术构建Mashup服务的特征向量，然后利用K-means算法对这些特征向量进行聚类。

LDA：该方法首先通过LDA模型将Mashup服务描述表示为主题向量的形式，进而选取向量主题概率最大的类别作为当前服务的类别标签，进行聚类。

L+K：该方法也是先通过LDA模型将Mashup服务描述表示为主题向量的形式。在此基础上，利用K-means算法对主题向量进行聚类。

F+K：该方法利用FSAC方法提取出每条Mashup服务描述（预处理后）的功能名词，并计算它们的功能语义权重。然后，选取功能语义权重较高的单词，结合TF-IDF模型与Word2Vec模型将它们表示成Mashup语义特征向量（简称MFSF向量），直接进行K-means聚类。

F+C+D: 该方法也是先将Mashup服务描述表示为MFSF向量，然后通过CCD-DI方法检测出最为合适的K个MFSF向量，以传统DPC算法实现聚类。

R+C+K：该方法首先利用Word2Vec模型将人工提取的功能名词转化为用于表示Mashup服务的文本向量，然后通过CCD-DI方法检测出最为合适的K个文本向量作为K-means的初始中心，进行聚类。

F+C+K：该方法也是先将Mashup服务描述表示为MFSF向量，然后通过CCD-DI方法检测出最为合适的K个MFSF向量作为K-means的初始中心，进行聚类。其中，CCD-DI方法中的权重参数a为默认值0.5。

其中，kmeans1.py是通过调用sklearn中的_k_means.py方法实现；kmeans2.py编程实现，可输入选定初始中心。lda.py中的实现代码采用_lda_.py实现，tfidf.py中tfidf_model的实现方法采用text.py实现。dpc.py采用传统dpc聚类算法实现Mashup服务聚类。manual.py通过读取人工提取的功能名词集RN.xlsx，直接利用Word2Vec进行Mashup服务文本向量的转化。