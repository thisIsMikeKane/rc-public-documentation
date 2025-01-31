(shell-environment-on-cluster)=

# Shell Environment on the Cluster

## The Discovery Shell environment and `.bashrc`

Discovery uses a Linux-based Operating System (CentOS), where the Shell program interfaces with the user. Bash (Bourne Again SHell) is one of the most popular Shell implementations, the default Shell on Discovery.

The Shell script `.bashrc` is used by Bash to initialize your Shell environment. For example, it is typically used to define aliases, functions, and load modules. Note that environment variables settings (such as `PATH`) generally go in the `.bash_profile` or `.profile` files. Your `.bashrc`, `.bash_profile`, and `.profile` files live in your `$HOME` directory. You can change your .bashrc with a text editor like [nano](https://www.nano-editor.org/).

:::{caution}
Making edits to your `.bashrc` file can result in many issues. Some changes may prevent you from launching apps or executing commands. Modifying your `PATH` variable may result in the inability to use basic Shell commands (such as `cd` or `ls`) if not done correctly.

Before making changes to your `.bashrc` file, make a backup of the default `.bashrc` file, so you can restore it if necessary. If you need help with editing `.bashrc`, reach out to <mailto:rchelp@northeastern.edu> or [schedule a consultation with a staff member](https://outlook.office365.com/owa/calendar/ResearchComputing2@northeastern.onmicrosoft.com/bookings/) who can help suggest edits and troubleshoot any issues you might be having.
:::

## About your .bashrc file

When your account is created, you have a default `.bashrc` file in your home directory. See the figure below for an example of a default `.bashrc` file.

```{image} ../images/catbashrc.jpg
```

:::{important}
We recommend keeping `.bashrc` unchanged when using Discovery. You can source environment Shell scripts or load modules directly inside your job instead. This approach can prevent some runtime errors from loading incompatible modules, setting environment variables incorrectly, or mixing multiple software and Conda environments.
:::

## Conda and `.bashrc`

In addition to editing your `.bashrc` file as outlined in the example above, programs you install can also modify your `.bashrc` file. For example, if you follow the procedure outlined in {ref}`mini-conda`, there may be a section added to your `.bashrc` file (if you didn't use the `-b` batch option) that automatically loads your conda environment every time you sign in to Discovery. See the figure below for an example of this:

:::{image} ../images/minicondabashrc.jpg
:::

You should not modify this section in the `.bashrc` file directly. If it was changed, remove this section manually using a file editor.

:::{caution}
We recommend removing the conda initialization section from your `.bashrc` as it may interfere with the correct startup environment when using Open OnDemand apps. You should always load your Conda environment after your job already started.
:::

If you need help with your `.bashrc` file or would like it restored to its default, reach out to the RC team at <mailto:rchelp@northeastern.edu>, and we can provide you with
a new default `.bashrc` file and help troubleshoot issues with the file.

### Editing your `.bashrc` file

The basic workflow for editing your `.bashrc` file is to sign in to Discovery, go to your `$HOME` directory, open the file in a text editor on the command line, make your edits, save the file, sign out of Discovery, then sign back in again. Your changes will take effect when you have signed back in again.

Example procedure for editing your `.bashrc` file:

1. Sign in to Discovery.

1. (Optional) Type `pwd` to ensure you are in your `/home` directory.

1. (Optional) Type `ls -a` to view the contents of your `/home` directory, including hidden files. Your `.bashrc` file is hidden (hidden files are preceded by a `.` ). Using the `-a` option with `ls` displays hidden files.

1. (Recommended) Type `cp .bashrc .bashrc-default` to make a copy of your `.bashrc` file called `.bashrc-default`.

1. Type `nano .bashrc` to open your `.bashrc` file in the nano text editor.

1. Type the edits that you want to make to your file. In this example, an alias was added to create a shortcut to the user's `/scratch` space.

   :::{image} ../images/nanobashrc.png
   :::
1. Save the file and exit the editor.
1. Sign out of Discovery and sign back in for the changes to take effect.

### Sourcing a Shell script example

A safe alternative to `.bashrc` is to source a Shell script inside your runtime job environment. Below is an example script to load an Anaconda module and source a Conda environment, which will be used inside the Slurm script.

Create a Shell script `myenv.bash`:

```{code-block} bash
#!/bin/bash
module load anaconda3/2021.05
module load cuda/11.1
source activate pytorch_env_training
```

Then, source the Shell script inside your sbatch Slurm script (see {ref}`using-sbatch`):

```{code-block} bash
#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --time=01:00:00
#SBATCH --job-name=gpu_run
#SBATCH --mem=4GB
#SBATCH --ntasks=1
#SBATCH --output=myjob.%j.out
#SBATCH --error=myjob.%j.err

source myenv.bash
python <myprogram>
```
