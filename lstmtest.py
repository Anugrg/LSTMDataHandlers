from sklearn import metrics
from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import layers




LSTM_model = tf.keras.models.load_model("/content/drive/My Drive/lstm models/Experiments/Experiment15/Model/G/LSTM_G.h5"  )
results = LSTM_model.evaluate(X_test, Y_test,batch_size=1)
print('results: ',results)

pred = LSTM_model.predict(X_test)
n_classes = 5

LABELS = [
    "SIT",
    "STAND",
    "WALK",
    "BEND",
    "FALL"
    ]

# LABELS = [ "Normal","FALL"]
precision, recall, f_score, support = metrics.precision_recall_fscore_support(Y_test.argmax(1), pred.argmax(1),average="weighted")

print("precision",100 * precision)
print("recall", 100 * recall)
print("f_score",100 * f_score)

print("number of occurrences of each class in test data", support)
print("confusion matrix")
confusion_matrix_basic = metrics.confusion_matrix(Y_test.argmax(1), pred.argmax(1))
print(confusion_matrix_basic)

cm = confusion_matrix(  Y_test.argmax(1), pred.argmax(1) )
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.colorbar()
tick_marks = np.arange(n_classes)
plt.xticks(tick_marks, LABELS, rotation=90)
plt.yticks(tick_marks, LABELS)
fmt = 'd'
thresh = cm.max() / 2.
for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
  plt.text(j, i, format(cm[i, j], fmt),
  horizontalalignment="center",
  color="white" if cm[i, j] > thresh else "black")

plt.tight_layout()
plt.ylabel('True label')
plt.xlabel('Predicted label')