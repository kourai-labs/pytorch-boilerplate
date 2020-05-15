import torch
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Export ONNX')
    parser.add_argument('-m', '--model', type=str, default=None,
            help="Path to pytorch model state dict (*.pth)."
    parser.add_argument('-i', '--input-shape', default=(1,3,224,224), type=int,
            help='Input shape (default: 224).')
    parser.add_argument('-o', '--output-name', default="model", type=str,
                        help='output model name (default: model.onnx )')
    args = parser.parse_args()

    raise NotImplemented

    # Load Pytorch model.
    model = None # init model here
    model.load_state_dict(torch.load(args.model))
    model.eval()

    # Do Pytorch -> ONNX conversion.
    inputs = torch.randn(args.input_shape)
    output_path = f'modules/{args.output_name}.onnx'
    torch.onnx.export(model, inputs, output_path)

    print(f'=== Exported {output_path} ===')

