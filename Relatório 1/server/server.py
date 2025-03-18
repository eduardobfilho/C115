import socket
import json

def load_questions():
    with open("questions.json", "r", encoding="utf-8") as file:
        return json.load(file)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(1)
    print("Servidor aguardando conexão...")
    
    conn, addr = server.accept()
    print(f"Cliente conectado: {addr}")
    
    # Carrega as questões do arquivo JSON
    questions = load_questions()
    
    # Envia as questões
    conn.sendall(json.dumps(questions).encode())
    
    # Recebe as respostas do cliente
    responses = json.loads(conn.recv(1024).decode())
    
    # Avalia as respostas
    result = []
    score = 0
    for i, response in enumerate(responses):
        correct = response == questions[i]["answer"]
        result.append({"question": questions[i]["question"], "correct": correct})
        if correct:
            score += 1
    
    # Envia o resultado para o cliente
    conn.sendall(json.dumps({"score": score, "details": result}).encode())
    
    conn.close()
    server.close()

if __name__ == "__main__":
    start_server()
