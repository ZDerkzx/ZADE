package main

import (
	"fmt"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"time"
)

func RnCommand(commands string, pause int) {
	commands = commands[1 : len(commands)-1]
	cnv_Commands := strings.Split(strings.ReplaceAll(commands, "\"", ""), ",")
	for _, value := range cnv_Commands {
		Cmd := exec.Command("cmd", "/C", value)
		err := Cmd.Run()
		if err != nil {
			fmt.Println("Error ejecutando el comando:",err)
		}
		time.Sleep(time.Duration(pause) * time.Second)
	}
}

func main() {
	if len(os.Args) < 1 {
		panic("Tecnicamente no hay nada...")
	}
	argumentos := os.Args[1]
	timer := os.Args[2]
	cnv_timer, err := strconv.Atoi(timer)
	if err != nil {
		panic(`Error: No se pudo convertir el str a int; Task: "task_executeCommands"`)
	}
	RnCommand(argumentos, cnv_timer)
}
