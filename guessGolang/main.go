package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
    // Seed the random number generator with the current Unix timestamp
    rand.Seed(time.Now().Unix())
	reader:=bufio.NewReader(os.Stdin)
    // Generate a random number
    randomNumber := rand.Intn(100) + 1 // Generates a random number between 1 and 100

    fmt.Println("Welcome to the guessing game!")
    fmt.Println("I've selected a random number between 1 and 100.")
    fmt.Println("Try to guess it!")
	//You can guess only 20 time!!!
	i:=0
    for i<20 {
		input1, _ := reader.ReadString('\n')
		int1, err := strconv.Atoi(strings.TrimSpace(input1))
		if err!=nil{
			println("unvalid input!")
			continue
		}
		if randomNumber>int1{
			fmt.Println("Guess higher please")
		}else if randomNumber<int1{
			fmt.Println("Guess lower please")
		}else{
			goto rightGuess
		}
		i++
		//your turns ended
		if i==20{
			fmt.Println("Times up!Our number is:",randomNumber)
		}
	}
rightGuess:
	fmt.Println("Thats right!Our number is:",randomNumber)
}