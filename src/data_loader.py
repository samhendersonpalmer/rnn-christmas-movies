class TextDataset(Dataset):
    """
    A class that accepts the samples which is a list of lists containing sequences of 64 words each.
    Also accepts word_to_int dictionary for mapping to integers.
    """
    def __init__(self, samples, word_to_int):
        self.samples = samples
        self.word_to_int = word_to_int
    def __len__(self):
        return len(self.samples)
    def __getitem__(self, idx):
        sample = self.samples[idx]
        input_seq = torch.LongTensor([self.word_to_int[word] for word in sample[:-1]])
        target_seq = torch.LongTensor([self.word_to_int[word] for word in sample[1:]])
        return input_seq, target_seq