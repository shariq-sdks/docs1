package utils

import (
	"os/exec"
	"strings"
)

// Checks if the output of a git stash operation indicates that the
// working directory was saved (i.e., something was actually stashed).
func IsStashed(output []byte) bool {
	// Check if the output of a git stash operation contains a message
	// indicating the command has been successfully done.
	return strings.Contains(string(output), "Saved working directory")
}

// Runs the equivalent of "git branch" with the provided arguments in
// the specified directory.
func RunGitBranch(dir string, args ...string) ([]byte, error) {
	return RunGitCommand(dir, "branch", args...)
}

// Runs the equivalent of "git stash" with the provided arguments in
// the specified directory.
func RunGitStash(dir string, args ...string) ([]byte, error) {
	return RunGitCommand(dir, "stash", args...)
}

// Runs the equivalent of "git checkout" with the provided arguments in
// the specified directory.
func RunGitCheckout(dir string, args ...string) ([]byte, error) {
	return RunGitCommand(dir, "checkout", args...)
}

// Executes a generic git command with the specified subcommand and
// arguments in the given directory. It returns the combined output of
// stdout and stderr.
func RunGitCommand(dir string, command string, args ...string) ([]byte, error) {
	// Wrap the command in new arguments.
	newArgs := append([]string{command}, args...)

	// Create a command to execute a "git" operation.
	cmd := exec.Command("git", newArgs...)

	// Configure the target directory.
	cmd.Dir = dir

	// Execute the command.
	return cmd.CombinedOutput()
}
