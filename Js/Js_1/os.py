import os       # For fork(), getpid(), getppid()
import signal   # For signal handling
import sys      # For sys.exit()
import time     # For sleep (to keep parent alive briefly)


# ─────────────────────────────────────────────
#  SIGNAL HANDLER
#  This function is called automatically when
#  the parent receives a SIGCHLD signal —
#  which the OS sends to the parent whenever
#  a child process terminates.
# ─────────────────────────────────────────────
def handle_child_termination(signum, frame):
    """
    Signal handler for SIGCHLD.
    
    Parameters:
        signum : The signal number (will be signal.SIGCHLD = 17)
        frame  : Current stack frame (not used here, but required by signal API)
    """
    print("\n[PARENT] ⚡ Signal received: Child process has terminated.")

    # os.wait() collects the exit status of the child process.
    # Without this, the child becomes a 'zombie process' — 
    # it's dead but still occupies a slot in the process table.
    child_pid, exit_status = os.wait()

    print(f"[PARENT] ✅ Cleaned up child process with PID: {child_pid}")
    print(f"[PARENT] 📋 Child exit status: {exit_status}")


# ─────────────────────────────────────────────
#  REGISTER THE SIGNAL HANDLER
#  We tell the OS: "When a child dies (SIGCHLD),
#  call our handle_child_termination function."
#  This must be set up BEFORE fork() is called.
# ─────────────────────────────────────────────
signal.signal(signal.SIGCHLD, handle_child_termination)


# ─────────────────────────────────────────────
#  FORK — Creating the Child Process
#
#  os.fork() splits the current process into two:
#    - In the CHILD  → fork() returns 0
#    - In the PARENT → fork() returns the child's PID
#
#  After fork(), both processes run the same code,
#  so we use the return value to tell them apart.
# ─────────────────────────────────────────────
print("[MAIN] 🚀 Forking process...")

pid = os.fork()  # This is where the magic happens!


# ─────────────────────────────────────────────
#  CHILD PROCESS BLOCK
#  pid == 0 means we are inside the child process
# ─────────────────────────────────────────────
if pid == 0:
    # os.getpid()  → returns this process's own PID
    # os.getppid() → returns the parent's PID
    my_pid    = os.getpid()
    parent_pid = os.getppid()

    print(f"\n[CHILD]  👶 I am the child process!")
    print(f"[CHILD]  🪪  My PID    : {my_pid}")
    print(f"[CHILD]  👨  Parent PID: {parent_pid}")
    print(f"[CHILD]  💤 Doing some work... (sleeping 2 seconds)")

    time.sleep(2)  # Simulate the child doing some work

    print(f"[CHILD]  🏁 Child work done. Exiting now.")

    # sys.exit(0) cleanly exits the child.
    # Exit code 0 = success.
    # This triggers SIGCHLD to be sent to the parent.
    sys.exit(0)


# ─────────────────────────────────────────────
#  PARENT PROCESS BLOCK
#  pid > 0 means we are inside the parent process
#  and pid holds the child's PID
# ─────────────────────────────────────────────
else:
    my_pid    = os.getpid()
    child_pid = pid  # fork() gave us the child's PID directly

    print(f"\n[PARENT] 👨 I am the parent process!")
    print(f"[PARENT] 🪪  My PID      : {my_pid}")
    print(f"[PARENT] 👶  Child's PID : {child_pid}")
    print(f"[PARENT] ⏳ Waiting for child to finish...\n")

    # Parent waits here. Meanwhile, the child runs.
    # When child exits, SIGCHLD fires → our handler runs.
    time.sleep(5)  # Give child enough time to complete

    print("\n[PARENT] 👋 Parent process is now finishing. Goodbye!")