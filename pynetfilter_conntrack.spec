Summary:	Manipulate conntrack objects
Name:		pynetfilter_conntrack
Version:	0.4.2
Release:	3
License:	GPLv2+
Group:		Networking/Other
Url:		http://pypi.python.org/pypi/pynetfilter_conntrack
Source0:	http://cheeseshop.python.org/packages/source/p/pynetfilter_conntrack/%{name}-%{version}.tar.bz2
BuildRequires:	python-devel
BuildRequires:	python-ipy
BuildRequires:	python-ctypes
BuildRequires:	python-elementtree
BuildRequires:	libnetfilter_conntrack-devel
Requires:	python-ipy
Requires:	python-ctypes
Requires:	python-elementtree
BuildArch:	noarch

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
%doc README AUTHORS
%{_bindir}/conntrack.py
%{py_puresitedir}/%{name}/*.py*
%{py_puresitedir}/*egg-info


%changelog
* Sat Feb 27 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-1mdv2010.1
+ Revision: 512400
- update to new version 0.4.2
- spec file clean
- update urls

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.4-5mdv2010.0
+ Revision: 441998
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.4-4mdv2009.0
+ Revision: 259444
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.4-3mdv2009.0
+ Revision: 247314
- rebuild
- fix summary-not-capitalized
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 12 2007 Michael Scherer <misc@mandriva.org> 0.4-1mdv2008.1
+ Revision: 97695
- new version 0.4


* Thu Nov 16 2006 Olivier Blin <oblin@mandriva.com> 0.2-1mdv2007.0
+ Revision: 84837
- buildrequires python-devel
- buildrequires libnetfilter_conntrack-devel
- buildrequires python-ctypes and python-elementtree
- buildrequires python
- remove useless echo
- initial pynetfilter_conntrack release
- Create pynetfilter_conntrack

