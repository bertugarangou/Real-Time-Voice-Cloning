Versió corregida per suportar UTF-8 en llengües com el **català**. 

## Carpeta Utilities
Conté dependències de Microsoft

## Carpeta venv-anaconda-conda
Conté el paquet del virtual enviroment d'Anaconda (Python)
____

# Real-Time Voice Cloning


### Papers implemented  
| URL | Designation | Title | Implementation source |
| --- | ----------- | ----- | --------------------- |
|[**1806.04558**](https://arxiv.org/pdf/1806.04558.pdf) | **SV2TTS** | **Transfer Learning from Speaker Verification to Multispeaker Text-To-Speech Synthesis** | This repo |
|[1802.08435](https://arxiv.org/pdf/1802.08435.pdf) | WaveRNN (vocoder) | Efficient Neural Audio Synthesis | [fatchord/WaveRNN](https://github.com/fatchord/WaveRNN) |
|[1703.10135](https://arxiv.org/pdf/1703.10135.pdf) | Tacotron (synthesizer) | Tacotron: Towards End-to-End Speech Synthesis | [fatchord/WaveRNN](https://github.com/fatchord/WaveRNN)
|[1710.10467](https://arxiv.org/pdf/1710.10467.pdf) | GE2E (encoder)| Generalized End-To-End Loss for Speaker Verification | This repo |

## Setup

### 1. Install Requirements
1. Descarregar i instal·lar la versió del SO més recent de [ffmpeg](https://ffmpeg.org/download.html#get-packages).
2. Dins la `carpeta venv-anaconda-conda`, activar l'enviroment amb `conda activate voice-clone`.

### 2. (Optional) Test Configuration
Before you download any dataset, you can begin by testing your configuration with: `python demo_cli.py`.

### 3. Launch the Toolbox
Arrencar l'eina amb `python demo_toolbox.py -d <datasets_root>` ó `python demo_toolbox.py`.
