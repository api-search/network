---
api_count: 11
apis:
- description: System calls for file and directory manipulation, including open, read, write, and file descriptor management.
  name: File System Operations API
  slug: ''
- description: System calls for process creation, execution, termination, and control.
  name: Process Management API
  slug: ''
- description: System calls for communication between processes including pipes, signals, and shared memory.
  name: Interprocess Communication API
  slug: ''
- description: System calls for memory allocation, mapping, and protection.
  name: Memory Management API
  slug: ''
- description: System calls for retrieving system information and configuration.
  name: System Information API
  slug: ''
- description: POSIX threads (pthreads) interface for creating and managing threads, mutexes, condition variables, and thread-specific data.
  name: POSIX Threads API
  slug: ''
- description: System calls for monitoring multiple file descriptors for readiness, enabling event-driven and non-blocking I/O patterns.
  name: I/O Multiplexing API
  slug: ''
- description: POSIX named and unnamed semaphore interfaces for process and thread synchronization.
  name: POSIX Semaphores API
  slug: ''
- description: POSIX message queue interfaces for exchanging messages between processes with priority support.
  name: POSIX Message Queues API
  slug: ''
- description: POSIX terminal interface (termios) and device control system calls for managing terminals, serial ports, and device parameters.
  name: Terminal and Device I/O API
  slug: ''
- description: POSIX advisory file locking interfaces for coordinating file access between processes.
  name: File Locking API
  slug: ''
common:
- title: ''
  type: Documentation
  url: https://pubs.opengroup.org/onlinepubs/9799919799/
- title: ''
  type: Documentation
  url: https://pubs.opengroup.org/onlinepubs/9699919799/
- title: ''
  type: Documentation
  url: https://man7.org/linux/man-pages/dir_section_2.html
- title: ''
  type: GettingStarted
  url: https://sourceware.org/glibc/manual/
- title: ''
  type: Resources
  url: https://en.wikipedia.org/wiki/POSIX
- title: ''
  type: APIReference
  url: https://unix.org/apis.html
- title: ''
  type: Documentation
  url: https://standards.ieee.org/ieee/1003.1/7700/
created: '2024-01-15'
description: Core UNIX/POSIX system calls providing low-level operating system interfaces for process management, file operations, interprocess communication, and system control.
features:
- File system operations and file descriptor management
- Process creation, execution, and control
- Interprocess communication via pipes, signals, and sockets
- Memory mapping and virtual memory management
- POSIX threads for concurrent programming
- I/O multiplexing with select and poll
- Named and unnamed semaphores
- Message queues for async process communication
- Terminal and device I/O control
- Advisory file locking
image: /assets/icons/unix.png
integrations:
- Linux kernel
- macOS / Darwin
- FreeBSD
- GNU C Library (glibc)
- musl libc
- POSIX-compliant operating systems
layout: provider
modified: '2026-04-18'
name: UNIX System Call
skills: []
slug: unix
solutions: []
tags:
- C-Api
- Ieee-1003
- Kernel
- Open-Group
- Operating-System
- Posix
- System-Calls
- Unix
url: https://raw.githubusercontent.com/api-evangelist/unix/refs/heads/main/apis.yml
use_cases:
- Operating system development
- Systems programming and embedded systems
- Network server and daemon development
- High-performance I/O applications
- Concurrent and multi-threaded programming
- Device driver and hardware interface development
---
