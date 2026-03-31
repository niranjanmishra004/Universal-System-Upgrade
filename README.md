<h1>⚙️ Universal-System-Upgrade </h1>

  <p>
    A <strong>cross-platform system update automation tool</strong> built in Python that 
    intelligently detects your operating system and runs the appropriate 
    <strong>update, upgrade, and cleanup commands</strong>.
  </p>

  <p>
    Supports <strong>Linux (Debian, Arch, RHEL)</strong>, <strong>macOS</strong>, and 
    <strong>Windows</strong> — making it a <strong>one-command solution</strong> to keep your system up to date.
  </p>

  <hr>

  <h2>✨ Features</h2>
  <ul>
    <li>🌍 <strong>Cross-Platform Support</strong>
      <ul>
        <li>Linux (Debian, Ubuntu, Kali, Arch, Fedora, etc.)</li>
        <li>macOS (Homebrew & system updates)</li>
        <li>Windows (winget / Chocolatey)</li>
      </ul>
    </li>
    <li>🔍 <strong>Automatic OS & Distro Detection</strong></li>
    <li>⚡ <strong>One-Command Full System Update</strong></li>
    <li>🧹 <strong>Auto Cleanup</strong> (remove unused packages & cache)</li>
    <li>🎨 <strong>Colorized Terminal Output</strong></li>
    <li>⏳ <strong>Interactive Spinner UI</strong></li>
    <li>❌ <strong>Error Handling & Safe Exit</strong></li>
    <li>🚀 <strong>Lightweight & No External Dependencies</strong></li>
  </ul>

  <hr>

  <h2>📸 Sample Output</h2>
  <p></p>

  <hr>

  <h2>🛠️ Supported Systems</h2>
  <ul>
    <li><strong>Debian-based:</strong> Ubuntu, Kali, Linux Mint, Pop!_OS</li>
    <li><strong>Arch-based:</strong> Arch Linux, Manjaro, EndeavourOS</li>
    <li><strong>RHEL-based:</strong> Fedora, CentOS, Rocky Linux, AlmaLinux</li>
    <li><strong>macOS:</strong> Homebrew / system updates</li>
    <li><strong>Windows:</strong> winget / Chocolatey</li>
  </ul>

  <hr>

  <h2>🚀 Installation & Usage</h2>

  <h3>1. Clone the repository</h3>
  <pre><code>git clone https://github.com/niranjanmishra004/Universal-System-Upgrade.git</code></pre>

  <h3>2. Navigate into the directory</h3>
  <pre><code>cd Universal-System-Upgrade</code></pre>

  <h3>3. Make it executable</h3>
  <pre><code>chmod +x update.py</code></pre>

  <h3>4. Run the script</h3>
  <pre><code>python3 update.py</code></pre>

  <p><strong>⚠️ Note:</strong> Some commands require <code>sudo</code> privileges.</p>

  <hr>

  <h2>⚙️ How It Works</h2>
  <ul>
    <li>Detects your OS using Python's <code>platform</code> module</li>
    <li>Identifies Linux distribution via <code>/etc/os-release</code></li>
    <li>Selects appropriate package manager:
      <ul>
        <li><code>apt</code> (Debian)</li>
        <li><code>pacman</code> (Arch)</li>
        <li><code>dnf / yum</code> (RHEL)</li>
        <li><code>brew</code> (macOS)</li>
        <li><code>winget / choco</code> (Windows)</li>
      </ul>
    </li>
    <li>Executes update → upgrade → cleanup automatically</li>
  </ul>

  <hr>

  <h2>📂 Project Structure</h2>
  <pre><code>
universal-updater/
│── updater.py
│── README.md
  </code></pre>

  <hr>

  <h2>🎯 Use Cases</h2>
  <ul>
    <li>🔧 Automating system maintenance</li>
    <li>🧑‍💻 DevOps environment setup</li>
    <li>⚡ Quick updates across multiple OS</li>
    <li>📚 Learning cross-platform scripting</li>
  </ul>

  <hr>

  <h2>🧠 Why This Project?</h2>
  <p>
    Instead of remembering different commands for different operating systems, this tool provides a <strong>single interface</strong> to manage updates everywhere.
  </p>



  <hr>

  <h2>🤝 Contributing</h2>
  <p>Contributions are welcome! Feel free to fork and submit a pull request.</p>

  <hr>

  <h2>⭐ Support</h2>
  <p>If you found this useful, consider giving it a ⭐ on GitHub!</p>
