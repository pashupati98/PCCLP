# polymer-property-prediction-using-machine-learning

Now-a-days machine learning is extensively being used by researchers to accelerate the development process of novel materials. Development of novel polymers can also be accelerated by using machine learning algorithms in many ways. 
i.e. <br/><br/>
1) Predicting properties of a novel polymer before actually synthesizing it in the laboratory.<br/>
2) Tuning the design of a polymer to have desired set of properties.<br/>
3) Extracting valuable information from failed experiments by traning ML models.<br/>
4) For accelerating material simulation & materials design models (CGM, PSO etc.)<br/>
So, whenever we have sufficient amount of data and we need to extract some valuable information from that or need to make some prediction, we can use appropriate machine learning algorithm.
<br/><br/>

**Disclaimer**<br/>This is the very initial documentation of the project which involves little information (which is open source) about it in order to keep things confidential. Codes uploaded are sample codes (Restricted and non-optimized)<br/>For Details write to : pgupta4@ch.iitr.ac.in
<br/><br/>

# Problem Statement
The problem on which this project is based on is predicting critical chain length of a desired polymer corresponding to its saturated solubility parameter.<br/><br/>
**Critical Chain Length & Saturated Solubility Parameter**<br/>
Solubility parameter of a polymer depends on its chain length and after a certain chain length it becomes saturated (no more significant change) *more details can be found in literature*<br/>

Now the issue is the calculation of this value which involves molecular simulations. This process is very slow, computesionaly expensive and inefficient. Our apporach is to solve this problem using machine learning so that we can directly predict the chain length at which the solubility parameter of a polymer will become saturated.
<br/><br/>
# Machine Learning based solution
So, we are trying to train a machine learning model on a dataset which is having the data of polymers and their critical chain length. The very first issue is making such dataset because we need all the data in mathematical form. We used group conribution theory and developed a python program which is used extract features from a repeting unit structure and make a fingerprint of that polymer using feature vectors and ultimately represents the polymer in numerical form. So, the processed dataset have numerical representation of a polymer and its critical chain length.<br/><br/>

</br>Next we are developing a machine learning model from scratch to learn the dependency of critical chain length on various features. Firstly we used linear hypothesis for this purpose because we need continuous outputs. Now we are working on support vector regression model to get better efficiency. We are also working on self evolving machine learning algorithms.
<br/><br/>
**Challenges**<br/>
1) Appropriate numerical representation of a polymer (Using some optimization algorithm)<br/>
2) Collecting sufficient amount of data (Using data augmentation techniques)<br/>
3) Optimizing number of features to train the model. (Literature Survey Going On)<br/>
4) Mapping function to map features vectors to desired property. (Literature Survey Going On)<br/><br/>

**Reference Links**<br/>
1) https://www.nature.com/articles/sdata201612<br/>
2) https://www.nature.com/articles/srep20952<br/>
3) https://www.tandfonline.com/doi/pdf/10.1080/08927022.2016.1269258<br/>
4) https://pubs.acs.org/doi/10.1021/acs.jpcc.8b02913<br/>
5) https://ws680.nist.gov/publication/get_pdf.cfm?pub_id=915933<br/>
6) https://www.nature.com/articles/s41467-018-08222-6<br/>
7) https://www.researchgate.net/publication/326608140_Machine_learning_for_molecular_and_materials_science<br/>
8) https://www.journals.elsevier.com/computational-materials-science/article-selection/recent-advances-on-materials-science-based-on-machine-learni



