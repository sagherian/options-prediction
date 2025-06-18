class OptionsModel:
    def __init__(self, input_dim, output_dim, hidden_dim=64, num_layers=2):
        import torch
        import torch.nn as nn
        
        self.model = nn.Transformer(
            d_model=input_dim,
            nhead=4,
            num_encoder_layers=num_layers,
            num_decoder_layers=num_layers,
            dim_feedforward=hidden_dim,
            dropout=0.1,
            activation='relu'
        )
        self.fc_out = nn.Linear(input_dim, output_dim)

    def forward(self, src, tgt):
        src_mask = self._generate_square_subsequent_mask(len(src)).to(src.device)
        tgt_mask = self._generate_square_subsequent_mask(len(tgt)).to(tgt.device)
        output = self.model(src, tgt, src_mask=src_mask, tgt_mask=tgt_mask)
        return self.fc_out(output)

    def _generate_square_subsequent_mask(self, sz):
        import torch
        return (torch.triu(torch.ones(sz, sz)) == 1).transpose(0, 1).float().masked_fill(torch.triu(torch.ones(sz, sz)) == 0, float('-inf'))

    def get_loss_function(self):
        import torch.nn as nn
        return nn.CrossEntropyLoss()

    def get_optimizer(self, learning_rate=0.001):
        import torch.optim as optim
        return optim.Adam(self.model.parameters(), lr=learning_rate)