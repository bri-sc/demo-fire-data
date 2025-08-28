## Global fire data demo

This is a Bristol Scientific Computing (BriSC) Python interactive demonstration. This provides a taster for the type of coding and approach we take on the "X with Computing" and "Scientific Computing with Data Science" programmes at the University of Bristol. See the [BriSC webpage](https://brisc.blogs.bristol.ac.uk/) and [Postgraduate Programme for Scientific Computing with Data Science](https://www.bristol.ac.uk/study/postgraduate/taught/msc-scientific-computing-with-data-science/) for more details.

This demo investigates satellite data of global fires (Fire Radiative Power) available from NASA and looks for interesting features of the data.

Click on this link to launch this through MyBinder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bri-sc/data-demo/HEAD?urlpath=%2Fdoc%2Ftree%2Fdemo.ipynb)

Note: this may take a while to load as MyBinder is building a coding environment for you to use in the cloud. This will not save any changes made to the file and will timeout after a few minutes of inactivity but can be relaunched.

Answer's notebook:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bri-sc/data-demo/HEAD?urlpath=%2Fdoc%2Ftree%2Fdemo_ans.ipynb)

The plotting code using the `folium` Python packaged used within the demo is available in the [map_maker.py](https://github.com/bri-sc/demo-fire-data/blob/main/map_maker.py) module file and the Jupyter notebook itself is [demo.ipynb](https://github.com/bri-sc/demo-fire-data/blob/main/demo.ipynb).

This demonstration makes use of the FIRMS database provided by NASA. Information for FIRMS can be found at  
https://www.earthdata.nasa.gov/engage/open-data-services-software-policies/data-use-policy

DISCLAIMER
LANCE is operated by the ESDIS Project. The information presented through LANCE, GIBS, Worldview, and FIRMS are 
provided and users bear all responsibility and liability for their use of data, 
and for any loss of business or profits, or for any indirect, incidental or consequential damages arising out of any use of, 
or inability to use, the data, even if NASA or ESDIS were previously advised of the possibility of such damages, 
or for any other claim by you or any other person. Due to the spatial resolution and other characteristics of these data, 
their use for tactical decision-making or informing about conditions at a local scale are not advised.
 
ESDIS makes no representations or warranties of any kind, express or implied, including implied warranties of fitness 
for a particular purpose or merchantability, or with respect to the accuracy of or the absence or the presence or defects 
or errors in data, databases of other information. The designations employed in the data do not imply 
the expression of any opinion whatsoever on the part of ESDIS concerning the legal or development status of any country, 
territory, city or area or of its authorities, or concerning the delimitation of its frontiers or boundaries. 
For more information please contact Earthdata Support: earthdata-support@nasa.gov.
