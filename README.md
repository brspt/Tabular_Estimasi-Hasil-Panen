# Tabular Estimasi Hasil Panen

Repository ini berisi notebook untuk pelatihan dan pemakaian model tabular estimasi hasil panen padi, beserta dataset dari Kaggle.

## Isi Repository

- `notebooks/training-tabular-rice-yield-model-pipeline.ipynb` - pipeline training model tabular.
- `notebooks/tabular-load-saved-model-single-training.ipynb` - notebook untuk load model tersimpan dan menjalankan prediksi/evaluasi single training.
- `data/Crop Yeild Data.csv` - dataset dari Kaggle: <https://www.kaggle.com/datasets/brspot/dataset2>

## Cara Menjalankan

1. Buat environment Python.
2. Install dependency:

```bash
pip install -r requirements.txt
```

3. Buka notebook di folder `notebooks/` menggunakan Jupyter Notebook, JupyterLab, atau Google Colab.
4. Pastikan path dataset diarahkan ke `data/Crop Yeild Data.csv` jika menjalankan secara lokal.

## Sumber Dataset

Dataset berasal dari Kaggle dataset `brspot/dataset2`.
