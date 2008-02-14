%define name pynetfilter_conntrack
%define version 0.4
%define release %mkrel 1

Summary: Manipulate conntrack objects
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://cheeseshop.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.bz2
License: GPL
Group: Networking/Other
Url: http://software.inl.fr/trac/trac.cgi/wiki/%{name}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-IPy
BuildRequires: python-ctypes
BuildRequires: python-elementtree
BuildRequires: libnetfilter_conntrack-devel
Requires: python-IPy
Requires: python-ctypes
Requires: python-elementtree

%description
This python library is based on libnetfilter_conntrack, which lets you
manipulate conntrack objects. In other words, pynetfilter_conntrack
lets you deal with Netfilter's stateful inspection objects from the
Python world.

Practically, for the administrator, this means you can now easily
close connections of your choice on your Linux [2.6] firewall. You can
also receive informations about all connections (how many packets have
gone through, how many bytes, etc.). You will even be able to create
new objects in the Connection Tracking (this means that complex
protocols such as FTP, P2P, etc. can have Python dealing with them
rather than complex kernel modules).

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/conntrack.py
%{py_puresitedir}/%{name}/*.py*
%{py_puresitedir}/*egg-info

