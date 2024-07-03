![Image](img/digital_logo_withwriting.png)
# Audio Mean Opinion Score (MOS) Evaluation Experiments Template

## Description
The Audio Mean Opinion Score (MOS) Evaluation Experiments Template project aims to assess the performance of deep learning models by gathering feedback from human evaluators. This README file provides detailed instructions on how to set up and run the project.

## Example
Example of the experiment can be found [MOS](https://keikinn.github.io/mos-template/rendered_mos) and [Comparison MOS](https://keikinn.github.io/mos-template/rendered_pair_comparison)


## Usage
1. Prepare the samples:
    - place all the audio files with their parent folder in the `wav` directory.

2. Prepare the filelist:
    - create a filelist in the `filelist` directory
    - the filelist should be a csv file with each line containing order and the path to an audio file. Please refer to the csv files in the directory 'filelist' for examples.

3. Run the project:
    - run `render_mos.py` or `render_pair_comparison.py` to generate the html file

4. set Github Pages
    - go to the repository settings and set the Github Pages

5. Share the link to the experiment

6. Collect the results:
    - the results will be downloaded as a json file. Please collect the results from the users

## Credits
This project is highly inspired by the [human-evaluation](https://github.com/yistLin/human-evaluation) project by [yistLin](https://github.com/yistLin)

## License
This project is licensed under the GNU GPLv3 License. See the [LICENSE](LICENSE) file for more details.
