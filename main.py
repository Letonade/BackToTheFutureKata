from adapters.cli_adapter import CLIInputAdapter, CLIOutputAdapter
from core.dvd_distributor import DvdDistributor
from application.dvd_distributor_cart_service import DvdDistributorCartService

if __name__ == "__main__":
    cart_input = """"""

# On part du principe que l'interface utilisateur la plus basique est un CLI
# car on recoit une ligne de texte.
    input_adapter = CLIInputAdapter(cart_input)
    output_adapter = CLIOutputAdapter()
    dvd_distributor = DvdDistributor()

# On à donc pour fonctionné notre input > distributor > output
# Le service regarde donc l'input et le distributor puis renvoie l'output
    cart_service = DvdDistributorCartService(input_adapter, output_adapter, dvd_distributor)

# Print incorporé à l'adapter de sortie
    total = cart_service.handle_cart() 
    
    
    cart_input = """Back to the Future 1
    Back to the Future 2
    Back to the Future 3"""
    input_adapter.set_cart(cart_input)
    total = cart_service.handle_cart()
    
    cart_input = """Back to the Future 1
    Back to the Future 3"""
    input_adapter.set_cart(cart_input)
    total = cart_service.handle_cart()
    
    cart_input = """Back to the Future 1"""
    input_adapter.set_cart(cart_input)
    total = cart_service.handle_cart()
    
    cart_input = """Back to the Future 1
    Back to the Future 2
    Back to the Future 3
    Back to the Future 2"""
    input_adapter.set_cart(cart_input)
    total = cart_service.handle_cart()

    
    cart_input = """Back to the Future 1
    Back to the Future 2
    Back to the Future 3
    La chèvre"""
    input_adapter.set_cart(cart_input)
    total = cart_service.handle_cart()
    