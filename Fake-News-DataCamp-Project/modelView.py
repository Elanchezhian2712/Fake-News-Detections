import pickle

# Specify the path to your .pkl file
file_path = 'best_model.pkl'

# Open the file in binary read mode ('rb')
with open(file_path, 'rb') as file:
    # Load the object from the pickle file
    loaded_object = pickle.load(file)

# Now, you can work with the loaded object as needed
print(loaded_object)
